#!/usr/bin/env python
# coding: utf-8

# ## Data Visualization

# - This notebook gives the layout scatter plot and violin plot functions 

# ### Function to plot scatter plot

# In[1]:


from dash.dependencies import html 
import dash
from dash.dependencies import dcc, dbc
import pandas as pd
import numpy as np
from data_pre_processing import pre_process_metadata
# In[2]:

# read the data files - chronos.csv, cn.csv, expression.csv, metadata.csv
chronos = pd.read_csv("chronos.csv")
cn = pd.read_csv("cn.csv")
expression = pd.read_csv("expression.csv")
metadata = pd.read_csv("metadata.csv")
metadataFiltered = pre_process_metadata(metadata)
# In[3]:
def draw_scatter_plot():
    '''
    This function gives the scatter plot between the variables (chronos/cn/expression) and the metadata in the app
    param : none
    return : html.Div element with the layout of the scatter plot 
    '''
    return html.Div(style = {'width' :'100%',
                             'height' : '100%'},
             children = [
                 # Specifying the field for the dropdown to select the variable (chronos, cn, expression) and metadata

                 # Specifying the field for the layout of the scatter plot
                    
                    html.Div(style = {
                                        'box-shadow' : '0 4px 8px 0 rgba(0, 0, 0, 0.4)',
                                        'textAlign' : 'center',
                                        'box-sizing' : 'border-box',
                                        'display' : 'flex'
                    },
                        children = [html.Div(
                        style = {
                            'box-shadow' : '0 4px 8px 0 rgba(0, 0, 0, 0.4)',
                            'textAlign' : 'left',
                            'box-sizing' : 'border-box',
                            'flex' : '20%',
                            'padding' : '10px 10px 10px 10px',
                        },
                        children = [
                            html.Div(
                                children = [
                                # Dropdown to select the variable field
                                html.Div(style = {'padding' : '0px 0px 10px 0px'},
                                    children = [
                                    html.Div(
                                        [
                                            html.H6("Select Chronos Field"),
                                            dcc.Dropdown(style = {"width" : "200px"},
                                                id = "change-chronos-field",
                                                options = [
                                                    {"label" : "{}".format(i), "value" : "{}".format(i)} for i in chronos.columns[1:]
                                                ],
                                                value = "TTC9B"
                                            ),
                                        ]
                                    )
                                 ]
                                ),
                                
                                # Dropdown to select the variable field
                                html.Div(style = {'padding' : '0px 0px 10px 0px'},
                                    children = [
                                    html.Div(
                                        [
                                            html.H6("Select Expression Field"),
                                            dcc.Dropdown(style = {"width" : "200px"},
                                                id = "change-expression-field",
                                                options = [
                                                    {"label" : "{}".format(i), "value" : "{}".format(i)} for i in expression.columns[1:]
                                                ],
                                                value = "TTC9B"
                                            ),
                                        ]
                                    )
                                  ]
                                ),
                                # Dropdown to select the metadata field
                                html.Div(style = {'padding' : '0px 0px 10px 0px'},
                                    children = [
                                    html.Div(
                                        [
                                            html.H6("Select metadata Field"),
                                            dcc.Dropdown(style = {"width" : "200px"},
                                                id = "change-metadata-field-scatter",
                                                options = [
                                                    {"label" : "{}".format(i), "value" : "{}".format(i)} for i in metadataFiltered.columns[1:]
                                                ],
                                                value = "sex"
                                            ),
                                        ]
                                    )
                                  ]
                                )
                              ]
                            )
                        ]
                    ),
                            html.Div(style = {'flex' : '3%'}),
                            html.Div(style = {'flex' : '77%'},
                                # plot the scatter plot
                                children = [
                                        html.Div(style = {
                                                'box-shadow' : '0 4px 8px 0 rgba(0, 0, 0, 0.4)',
                                                'textAlign' : 'center',
                                                'box-sizing' : 'border-box',
                                            },
                                            children = [
                                                dcc.Graph(
                                                    id = "scatterPlot"
                                                )
                                            ]
                                    )
                                ]
                            )
                        ]
                    )
                ]
            )

# ### Function to plot the violin plot

# In[5]:


def draw_violin_plot():
    '''
    This function gives the violin plot between the variables (chronos/cn/expression) and the metadata
    param : none
    return : html.Div element with the layout of the violin plot 
    '''
    return html.Div(style = {'width' :'100%',
                             'height' : '100%'},
             children = [
                 # Specifying the field for the dropdown to select the variable (chronos, cn, expression) and metadata

                 # Specifying the field for the layout of the scatter plot
                    
                    html.Div(style = {
                                        'box-shadow' : '0 4px 8px 0 rgba(0, 0, 0, 0.4)',
                                        'textAlign' : 'center',
                                        'box-sizing' : 'border-box',
                                        'display' : 'flex'
                    },
                        children = [html.Div(
                        style = {
                            'box-shadow' : '0 4px 8px 0 rgba(0, 0, 0, 0.4)',
                            'textAlign' : 'left',
                            'box-sizing' : 'border-box',
                            'flex' : '20%',
                            'padding' : '10px 10px 10px 10px',
                        },
                        children = [
                            html.Div(
                                children = [
                                # Dropdown to select the Gene field
                                html.Div(
                                    children = [
                                    html.Div(
                                        [
                                            html.H6("Select Gene"),
                                            dcc.Dropdown(style = {"width" : "200px"},
                                                id = "change-gene",
                                                options = [
                                                    {"label" : "{}".format(i), "value" : "{}".format(i)} for i in chronos.columns[1:]
                                                ],
                                                value = "TTC9B"
                                            ),
                                        ]
                                    )
                                 ]
                                ),
                                # Dropdown to select the dataset field
                                html.Div(
                                    children = [
                                    html.Div(
                                        [
                                            html.H6("Select Dataset"),
                                            dcc.Dropdown(style = {"width" : "200px"},
                                                id = "change-dataset",
                                                options = [
                                                    {"label" : "{}".format(i), "value" : "{}".format(i)} for i in ['chronos', 'expression', 'cn']
                                                ],
                                                value = "chronos"
                                            ),
                                        ]
                                    )
                                  ]
                                ),
                                # Dropdown to select the metadata field
                                html.Div(
                                    children = [
                                    html.Div(
                                        [
                                            html.H6("Select Metadata Field"),
                                            dcc.Dropdown(style = {"width" : "200px"},
                                                id = "change-metadata-field-violin",
                                                options = [
                                                    {"label" : "{}".format(i), "value" : "{}".format(i)} for i in metadataFiltered.columns[1:]
                                                ],
                                                value = "sex"
                                            ),
                                        ]
                                    )
                                  ]
                                )
                              ]
                            )
                        ]
                    ),
                            html.Div(style = {'flex' : '3%'}),
                            html.Div(style = {'flex' : '77%'},
                                # plot the scatter plot
                                children = [
                                        html.Div(style = {
                                                'box-shadow' : '0 4px 8px 0 rgba(0, 0, 0, 0.4)',
                                                'textAlign' : 'center',
                                                'box-sizing' : 'border-box',
                                            },
                                            children = [
                                                dcc.Graph(
                                                    id = "violinPlot"
                                                )
                                            ]
                                    )
                                ]
                            )
                        ]
                    )
                ]
            )



# ### Function to plot the layout of scatter plot and violin plot

# In[1]:


# Function to plot the layout of scatter plot and violin plot

def draw_plots():
    '''
    This function gives the layout of the scatter plot and violin plot between the variables 
    (chronos/cn/expression) and the metadata
    param : none
    return : html.Div element with the layout of the scatter plot 
    '''
    # Getting the html Div element of violin and scatter plot with specified style 
    dark_button_style = {'background-color': '#6E8898FF',
                        'color': '#D3D0CBFF',
                        'height': '40px',
                        'width': '175px',
                        "font-weight" : "bolder",
                        'text-align' : 'left',
                        "font-weight" : "bolder",
                        'padding-left' : '50px',
                        "border" : "none",
                        "border-radius" : "2px"}
    light_button_style = {'background-color': '#6E8898FF',
                        'color': '#D3D0CBFF',
                        'height': '40px',
                        'width': '175px',
                        "font-weight" : "bolder",
                        'text-align' : 'left',
                        "font-weight" : "bolder",
                        'padding-left' : '50px',
                        "border" : "none",
                        "border-radius" : "2px"}
    return html.Div(style = {
            'margin' : '30px 30px 30px 30px',
            'box-shadow' : '0 4px 8px 0 rgba(0, 0, 0, 0.4)',
            'textAlign' : 'center',
            'box-sizing' : 'border-box',
            "width" : "1050px",
            "height" : "550px"
        },
            children = [
                html.Div([
                    html.Div(style = {'display' : 'flex',
                                     'width' : '100%',
                                     'padding' : '0px 0px 20px 0px'},
                    children = [
                        html.Div(style = {"flex" : "15%"},
                                  children = [
                                      html.Button(id='scatter-plot-layout-button',
                                                    children=['Scatter Plot'],
                                                    n_clicks=0,
                                                    style = dark_button_style
                                      )
                                  ]
                              ),
                        html.Div(style = {"flex" : "15%"},
                                  children = [
                                      html.Button(id='violin-plot-layout-button',
                                                    children=['Violin Plot'],
                                                    n_clicks=0,
                                                    style = light_button_style
                                      )
                                  ]
                              ),
                        html.Div(style = {"flex" : "70%"})
                    ]
                )
            ]),
            html.Div(id = "layout-plot")
            ]
        )

