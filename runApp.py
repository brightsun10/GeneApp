#!/usr/bin/env python
# coding: utf-8

# ## Run App

# - This notebook runs and displays the dash app 

# ### Installing and Importing libraries

# In[ ]:

# Installing the required libraries
# pip install dash
# pip install dash-core-components
# pip install dash-html-components
# pip install dash-renderer
# pip install dash-table
# pip install plotly
# pip install dash_bootstrap_components


# In[38]:


# Importing libraries
import pandas as pd
import pandas as pd
import numpy as np
import dash
from dash.dependencies import callback_context, Output, Input, dcc, dbc, html, dash_table
import plotly.express as px
import plotly.graph_objs as go
import re


# In[39]:


# Importing the homePageHeaderTitle, Dataoverview, DataVisualization, data preprocessing
from homepage_header_title import header, title_menu, home_page
from data_overview import data_overview_page
from data_visualization import draw_plots, draw_scatter_plot, draw_violin_plot
from data_pre_processing import pre_process_metadata


# ### Reading Data Files

# In[40]:


# read the data files - chronos.csv, cn.csv, expression.csv, metadata.csv
chronos = pd.read_csv("chronos.csv")
cn = pd.read_csv("cn.csv")
expression = pd.read_csv("expression.csv")
metadata = pd.read_csv("metadata.csv")


# ### App Layout

# In[41]:


app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

colors = {
    'background' : '#FFFFFF',
    'text' : '#7FDFF' 
}

dataframe = {'chronos' : chronos.head(20),
             'cn' : cn.head(20), 
             'expression' : expression.head(20), 
             'metadata' : metadata.head(20)}


# In[43]:


app.layout = html.Div(style = {'backgroundColor' : colors['background'],
                               'width' : '1365px',
                               },
                      children = [
                          header(),
                          html.Div(style = {"display" : "flex"},
                              children = [
                                  title_menu(),
                                  html.Div(style = {"flex" : "83%"},
                                              id = "page-layout"
                                          )
                              ]
                          )
                      ])
# @app.callback(Output('dashboard-button', 'style'),
#               Output('data-overview-button', 'style'),
#               Output('data-visualization-button', 'style'),
#               [Input('dashboard-button', 'n_clicks'),
#                Input('data-overview-button', 'n_clicks'),
#                Input('data-visualization-button', 'n_clicks')])
# def change_button_style(n_clicks_dashboard, n_clicks_dataoverview, n_clicks_datavisualization):
#     if n_clicks_dashboard > 0:
@app.callback(
    Output("page-layout", "children"), 
    [Input("dashboard-button", "n_clicks"),
     Input("data-overview-button", "n_clicks"),
     Input("data-visualization-button", "n_clicks")]
)
def display_page(n_click_dashboard, n_click_dataoverview, n_click_datavisulaization):
    changed_id = [p['prop_id'] for p in callback_context.triggered][0]
    if n_click_dashboard in changed_id:
        return home_page()
    elif n_click_dataoverview in changed_id:
        return data_overview_page()
    elif n_click_datavisulaization in changed_id:
        return draw_plots()
    else:
        return home_page()
        
    
@app.callback(
    Output("table", "children"), [Input("change-table", "value")]
)
def change_table(value):
    return html.Div(
        
        children = [
        dash_table.DataTable(
        columns=[{"name": i, "id": i, "selectable": True} for i in dataframe[value].columns],
        data=dataframe[value].to_dict('records'),
        sort_action="native",
        sort_mode="multi",
        column_selectable="single",
        selected_columns=[],
        selected_rows=[],
        style_cell_conditional = [
            {
                'if' : {'column_id' : c},
                
            } for c in dataframe[value].columns
        ],
        style_data = {
            'color' : 'black',
            'backgroundColor' : 'white',
            'textAlign' : 'left',
        },
        style_data_conditional = [
            {
                'if' : {'row_index' : 'odd'},
                'backgroundColor' : 'rgb(220, 220, 220)',
            }
        ],
        style_header = {
            'backgroundColor' : '#73A5C6',
            'color' : 'white',
            'fontWeight' : 'bold',
            'textAlign' : 'right'
        }
        )])   

@app.callback(
    Output("violinPlot", "figure"), 
    Input("change-gene","value"),
    Input("change-dataset","value"),
    Input("change-metadata-field-violin","value")
)
def update_violinPlot(change_gene_value, change_dataset_value, change_metadata_field_value):
    df = dataset[change_dataset_value]
    fig1 = px.violin(df, y=metadataFiltered[change_metadata_field_value], x=change_gene_value, 
                    color=metadataFiltered[change_metadata_field_value], 
                    box=True, points="all",

                    )
    
    return fig1

@app.callback(
    Output("scatterPlot", "figure"), 
    Input("change-chronos-field","value"),
    Input("change-expression-field","value"),
    Input("change-metadata-field-scatter","value")
)
def update_scatterPlot(change_chronos_field_value, change_expression_field_value, change_metadata_field_value):
    fig2 = px.scatter(chronos, 
                     x = chronos[change_chronos_field_value],
                     y = expression[change_expression_field_value],
                     color = metadataFiltered[change_metadata_field_value],
                     title = "Automatic Column Names Based on Dataframe")
    return fig2


# ### Running App

# In[ ]:


if __name__ == '__main__':
    app.run_server(debug = True, use_reloader = False)

