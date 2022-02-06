import json
import random

import pandas as pd


def create_data_set_dict(df, title, data_key, hover_name_key, dropdown_label, dropdown_value):
    return {
        'df': df,
        'title': title,
        'data_key': data_key,
        'hover_name_key' : hover_name_key,
        'dropdown_label': dropdown_label,
        'dropdown_value': dropdown_value
    }

def add_gml_id_to_df(df, _ortsteile_id_map, ortsteil_key_in_df='Ortsteil'):
    df['id'] = df[ortsteil_key_in_df].apply(lambda ortsteil: _ortsteile_id_map[ortsteil])


def get_berlin_population_density_data(ortsteile_id_map):

    cols_list = ["Ortsteil", "Einwohner"]
    df = pd.read_csv("resources\datasets\Ortsteil_Pop.csv", names=cols_list, header=1)

    add_gml_id_to_df(df, ortsteile_id_map)

    title = 'Berlin Population Density - absolute'
    data_key = 'Einwohner'
    hover_name_key = 'Ortsteil'
    dropdown_label = title
    dropdown_value = 'dp_value_1'

    data_set_dict = create_data_set_dict(
        df, title, data_key, hover_name_key, dropdown_label, dropdown_value
    )

    return dropdown_value, data_set_dict


def get_school_numbers(ortsteile_id_map):

    cols_list = ["Ortsteil", "Schulen"]
    df = pd.read_csv("resources\datasets\SchoolNumbers.csv", names=cols_list, header=1)

    # random.seed(1)
    # df['Einwohner'] = df['Einwohner'].apply(lambda x: x * random.random())

    add_gml_id_to_df(df, ortsteile_id_map)

    title = 'Number of Schools per District'
    data_key = 'Schulen'
    hover_name_key = 'Ortsteil'
    dropdown_label = title
    dropdown_value = 'dp_value_2'

    data_set_dict = create_data_set_dict(
        df, title, data_key, hover_name_key, dropdown_label, dropdown_value
    )

    return dropdown_value, data_set_dict


def get_rents(ortsteile_id_map):

    cols_list = ["Ortsteil", "Mietpreise"]
    df = pd.read_csv("resources\datasets\Miete.csv", names=cols_list, header=1)


    add_gml_id_to_df(df, ortsteile_id_map)

    title = 'Rent per Sq. Meter'
    data_key = 'Mietpreise'
    hover_name_key = 'Ortsteil'
    dropdown_label = title
    dropdown_value = 'dp_value_3'

    data_set_dict = create_data_set_dict(
        df, title, data_key, hover_name_key, dropdown_label, dropdown_value
    )

    return dropdown_value, data_set_dict


def get_parks(ortsteile_id_map):

    cols_list = ["Ortsteil", "ParkCount"]
    df = pd.read_csv("resources\datasets\Parks.csv", names=cols_list, header=1)


    add_gml_id_to_df(df, ortsteile_id_map)

    title = 'Number of Parks'
    data_key = 'ParkCount'
    hover_name_key = 'Ortsteil'
    dropdown_label = title
    dropdown_value = 'dp_value_4'

    data_set_dict = create_data_set_dict(
        df, title, data_key, hover_name_key, dropdown_label, dropdown_value
    )

    return dropdown_value, data_set_dict


def get_data_template(ortsteile_id_map):
    """
    This is only a template to demonstrate how the system works.

    The function must be add to "data_set_getter_functions" list. It will
    then automatically integrated into the system if it is setup correct.
    """
    # ...load and process your data

    # add the gml_id´s to the data frame so that plotly choropleth function can map ortsteile
    # to the map
    # add_gml_id_to_df(df, ortsteile_id_map)

    # pass all the needed data to this function in order to wrap the data so
    # that the app can further use it
    # df: the pandas data frame
    # title: a chosen title that gets displayed above the map
    # data_key: the actual data that should be projected onto the map, e.g. population
    # dropdown_label: the label that get displayed in dropdown menu for selecting this dataset
    # dropdown_value: basically an id for the dataset that gets used by the dropdown menu to select the dataset. must be unique!
    # data_set_dict = create_data_set_dict(
    #     df, title, data_key, hover_name_key, dropdown_label, dropdown_value
    # )

    # return the like this!
    # return dropdown_value, data_set_dict

    # remove
    pass


def load_data():

    berlin_ortsteile_geojson = json.load(open("resources\lor_ortsteile.geojson", "r", encoding='utf-8'))

    # create ortsteil id map -> {ortsteil: gml_id_of_ortsteil}
    ortsteile_id_map = {
        ortsteil_geo_obj["properties"]["OTEIL"]: ortsteil_geo_obj["properties"]["gml_id"]
        for ortsteil_geo_obj in berlin_ortsteile_geojson["features"]
    }

    all_data = {}
    for data_set_getter in data_set_getter_functions:
        dataset_dropdown_value, dataset_dict = data_set_getter(ortsteile_id_map)

        all_data[dataset_dropdown_value] = dataset_dict

    return all_data


data_set_getter_functions = [
    get_berlin_population_density_data,
    get_school_numbers,
    get_rents,
    get_parks
]