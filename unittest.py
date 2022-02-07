import unittest
from sklearn import preprocessing
import numpy as np

from data_factory import get_berlin_population_density_data



scaler = preprocessing.MinMaxScaler()


class testDataLoader(unittest.TestCase):

    def main_test(self):
        self.assertEqual(get_berlin_population_density_data(ortsteile_id_map,()))


# def get_berlin_population_density_data(ortsteile_id_map):

#     cols_list = ["Ortsteil", "Einwohner"]
#     df = pd.read_csv("resources\datasets\Ortsteil_Pop.csv", names=cols_list, header=1)

#     add_gml_id_to_df(df, ortsteile_id_map)

#     title = 'Berlin Population Density - absolute'
#     data_key = 'Einwohner'
#     hover_name_key = 'Ortsteil'
#     dropdown_label = title
#     dropdown_value = 'dp_value_1'

#     data_set_dict = create_data_set_dict(
#         df, title, data_key, hover_name_key, dropdown_label, dropdown_value
#     )

#     return dropdown_value, data_set_dict



    #     class TestCalculator(unittest.TestCase):

    # def add_test(self):
    #     self.assertEqual(calculator.add(1, 5), 6)
