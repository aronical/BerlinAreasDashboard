# visit http://127.0.0.1:8050/ 

import json
from math import ceil
from pydoc import classname
from tkinter import CENTER
import dash

import dash_bootstrap_components as dbc

from dash import dcc
from dash import html
from dash.dependencies import Input, Output

import plotly.express as px
import pandas as pd

from data_factory import load_data

import numpy as np
from sklearn import preprocessing


app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

berlin_ortsteile_geojson = json.load(open('resources\lor_ortsteile.geojson', 'r', encoding='utf-8'))




# load all data from the factory
all_dataset_dicts = load_data(berlin_ortsteile_geojson)

# create the dropdown options for switching data in the map
dropdown_options = [
    {'label': dataset_dict['dropdown_label'], 'value': dataset_dict['dropdown_value']}
    for dataset_dict in all_dataset_dicts.values()
]


dropdown_options.append({'label': 'Living Score', 'value': 'score_option'})

app.layout = html.Div(children=[

    html.H1(children='Berlin Districts Family Living: An Urban Technology Project'),
    html.Div(children='Choose your data:'),

    dcc.Dropdown(
        id='data-source',
        options=dropdown_options,
        value=dropdown_options[0]['value']  # initial value (data) to load
    ),


    html.Div(className='HorizontalBlock',style= {'display': 'flex', 'width': '80%', 'margin': '10px auto 50px 10px'}, children=[

            #visual adjustments for the graph
        html.Div(children=[
            dcc.Graph(
                id='map-graphic',
                style= {'margin-top':'1%'},
                
            )] 
        ),

                
     html.Div(className='SliderBlock',style= {'display': 'flex','flex-direction': 'column', 'flex-grow': '0.7', 'margin-left': '50px', 'justify-content': 'center'},children=[


        html.Div(className='SingleSliderCont',children=[

            html.Div(children=['Population Density:'],className='FlexChildTitle'),

            dcc.Slider(

                id='Slider1',
                vertical=False,
                className='FlexChild',
                step=1,
                min=1,
                max=3,
                value=1,
                marks={
                    1: {'label': 'Not Important'},
                    2: {'label': 'Less is better', 'style': {'color': '#77b0b1'}},
                    3: {'label': 'More is better', 'style': {'color': '#77b0b1', 'padding-left':'5%', 'white-space': 'nowrap'}},
                },
                included=False
            ),


        ]),

    
        html.Div(className='SingleSliderCont',children=[

            html.Div(children=['Number of Schools:'],className='FlexChildTitle'),

            dcc.Slider(
                id='Slider2',
                className='FlexChild',
                step=None,
                vertical=False,
                min=0,
                max=2,
                value=1,
                marks={
                    0: {'label': 'Not Important', 'style': {'color': '#77b0b1'}},
                    1: {'label': 'Important'},                  
                    2: {'label': 'Very Important', 'style': {'color': '#77b0b1', 'padding-left':'5%', 'white-space': 'nowrap'}},
                },
                included=False),

                    
             ]),


             html.Div(className='SingleSliderCont',children=[

                html.Div(children=['Rent Prices:'],className='FlexChildTitle'),

                dcc.Slider(
                id='Slider3',
                className='FlexChild',
                vertical=False,
                min=1,
                max=3,
                value=2,
                marks={
                    1: {'label': 'Not Important', 'style': {'color': '#77b0b1', 'padding-left':'5%', 'white-space': 'nowrap'}},
                    2: {'label': 'Important'},
                    3: {'label': 'Very Important', 'style': {'color': '#77b0b1', 'white-space': 'nowrap'}},
                
                },
                
                included=False)

               
             ]),


             html.Div(className='SingleSliderCont',children=[

                html.Div(children=['Number of Parks with Playgrounds:'],className='FlexChildTitle'),

                dcc.Slider(
                id='Slider4',
                className='FlexChild',
                vertical=False,
                min=0,
                max=2,
                value=1,
                marks={
                    0: {'label': 'Not Important', 'style': {'color': '#77b0b1'}},
                    1: {'label': 'Important'},
                    2: {'label': 'Very Important', 'style': {'color': '#77b0b1', 'padding-left':'5%', 'white-space': 'nowrap'}},
                },
                
                included=False)

             ]),

        ]),      

    ]),
    
], 

style={'margin': '0 15% 0 15%'}, 


)

@app.callback(
    Output('map-graphic', 'figure'),
    Input('data-source', 'value' ),
    Input('Slider1', 'value'),
    Input('Slider2', 'value'),
    Input('Slider3', 'value'),
    Input('Slider4', 'value')

)

def update_graph(dataset_dropdown_value, Slider1, Slider2, Slider3, Slider4):

    if dataset_dropdown_value == 'score_option':

#storing each data table in individual variables

        data_keys = list(all_dataset_dicts.keys())
        dataset1 = all_dataset_dicts[data_keys[0]]['df']['Einwohner']
        dataset2 = all_dataset_dicts[data_keys[1]]['df']['Schulen']
        dataset3 = all_dataset_dicts[data_keys[2]]['df']['Mietpreise']
        dataset4 = all_dataset_dicts[data_keys[3]]['df']['ParkCount']



        def normalize(dataset):
            scaler = preprocessing.MinMaxScaler()
            np_list = dataset.values.reshape(-1,1)
            normalized_list=scaler.fit_transform(np_list)
            return(normalized_list)
            

        #Slider Values Re-Definition for Score Calculation and Slider Mark Position Adjustment
        if (Slider1 == 1):
            Slider1 = 0
        elif(Slider1 == 2):
            Slider1 = -1
        elif (Slider1 == 3):
            Slider1 = 1



        if (Slider3 == 1):
            Slider3 = 0
        elif(Slider3 == 2):
            Slider3 = -1
        elif (Slider3 == 3):
            Slider3 = -2


        score = normalize(dataset1)*Slider1 + normalize(dataset2)*Slider2 + normalize(dataset3)*Slider3 + normalize(dataset4)*Slider4


        id_dataset = all_dataset_dicts[data_keys[0]]['df']

      
        score_df = pd.Series(score.flatten())

        print(type(score_df))


        score_dataset = pd.concat([score_df,id_dataset],axis=1)


        score_dataset.columns = ['score','Ortsteil','Einwohner','id']
        final_dataset = score_dataset
        color_key ='score'



    else:
        selected_dataset = all_dataset_dicts[dataset_dropdown_value]
        final_dataset = selected_dataset['df']
        color_key = selected_dataset['data_key']

    

 
    fig = px.choropleth(
        final_dataset,
        locations='id',
        # if not "featureidkey" is used plotly uses automatically "id" in "properties" of geojson obj
        featureidkey='properties.gml_id',
        geojson=berlin_ortsteile_geojson,
        color=color_key,
        hover_name = 'Ortsteil',
        hover_data = {'id':False},
        template = 'none',
        # color='score',
        # hover_name=selected_dataset['hover_name_key'],
        # hover_data=[selected_dataset['data_key']],
        # title=selected_dataset['title'],
    )

    # zoom map to existing data
    fig.update_layout(margin={'r': 0, 't': 0, 'l': 0, 'b': 0}),
    fig.update_geos(fitbounds='locations', visible=False)



    return fig


if __name__ == '__main__':
    app.run_server(debug=True)


