#!/usr/bin/env python
# coding: utf-8

# ## Data Overview 

# - This notebook gives the laout of the data overview page 

# ### Function to plot the data overview layout

# In[1]:


from dash import html 
import dash
import dash_bootstrap_components as dbc
from dash import dcc
from dash import dash_table
import pandas as pd
from data_pre_processing import pre_process_metadata
chronos = pd.read_csv("chronos.csv")
cn = pd.read_csv("cn.csv")
expression = pd.read_csv("expression.csv")
metadata = pd.read_csv("metadata.csv")
metadataFiltered = pre_process_metadata(metadata)
dataframe = {'chronos' : chronos.head(20),
             'cn' : cn.head(20), 
             'expression' : expression.head(20), 
             'metadata' : metadata.head(20)}
# In[ ]:

def data_overview_page():
    '''
    this function gives the layout of the data overview page in the app
    param: none
    return : Gives the Layout of the data overview page 
    '''
    return html.Div(style = {'margin' : '20px 20px 20px 20px',
                             "width" : "1050px"},
                              children = [
                                          # Specify the style to select dropdown to select the table 
                                          html.Div(style = {"display" : "flex"},
                                              children = [
                                                  html.Div(
                                                      style = {
                                                          'backgroundColor' : '#00000',
                                                          'flex' : '25%',
                                                          'height' : '155px',
                                                          'textAlign' : 'center',
                                                          'box-shadow' : '0 4px 8px 0 rgba(0, 0, 0, 0.4)',
                                                          'padding' : '1%',
                                                          'box-sizing' : 'border-box'
                                                      },
                                                      children = [
                                                          # Dropdown to select the dataset to display
                                                          html.Div(style = {'color' : '#6E8898FF',
                                                                            'font-weight' : 'bold',
                                                                            'text-align' : 'left',
                                                                           },
                                                                   children = [
                                                                       html.H4("Select Table"),
                                                                   ]),
                                                          dcc.Dropdown(
                                                              id = "change-table",
                                                              options = [
                                                                  {"label" : "chronos", "value" : "chronos"},
                                                                  {"label" : "cn", "value" : "cn"},
                                                                  {"label" : "expression", "value" : "expression"},
                                                                  {"label" : "metadata", "value" : "metadata"}
                                                              ],
                                                              value = "chronos"
                                                          ),
                                                          html.Div(
                                                                children = [
                                                                    html.Button(style = {
                                                                                "border" : "none",
                                                                                "backgroundColor" : "#6E8898FF",
                                                                                "width" : "230px",
                                                                                "height" : "35px",
                                                                                "color" : "#D3D0CBFF",
                                                                                "margin" : "20px 0px 20px 0px",
                                                                                "border-radius" : "2px",
                                                                                "font-weight" : "bold"
                                                                              },
                                                                                children = ["Download Dataset"], id="btn_csv"),
                                                                    dcc.Download(id="download-dataframe-csv"),
                                                                ]
                                                            )
                                              ]
                                          ),
                                          html.Div(style = {"flex" : "2%"}),
                                          html.Div(style = {"flex" : "73%"},
                                                  children = [

                                                      html.Div(style = {
                                                          "text-align" : "center",
                                                          
                                                      }, 
                                                    id = "summary-statistics")
                                                  ]),
                                          ]),
                                          html.Div(style = {"height" : "10px"}),
                                          # Specify the style of the dataset to be displayed
                                          html.Div([
                                          html.Div(
                                          style = {
                                              'overflowY' : 'scroll',
                                              'padding' : '1%',
                                              'backgroundColor' : '#00000',
                                              'box-shadow' : '0 4px 8px 0 rgba(0, 0, 0, 0.4)',
                                              'textAlign' : 'center',
                                              'maxHeight' : '400px',
                                              'box-sizing' : 'border-box'
                                          },
                                              # Display the dataset
                                          children = [
                                              html.Div(id = "table")
                                          ]
                                      )
                                  ])
                              ]
                          )