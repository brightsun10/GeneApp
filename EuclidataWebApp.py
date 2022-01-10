#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().system('python -m pip install -r info.txt')
get_ipython().system('pip install --upgrade dash dash-core-components dash-html-components dash-renderer')
get_ipython().system('pip install dash_bootstrap_components')


# In[1]:


# import the libraries
import pandas as pd
from dash import callback_context


# In[2]:


# read the data files - chronos.csv, cn.csv, expression.csv, metadata.csv
chronos = pd.read_csv("chronos.csv")
cn = pd.read_csv("cn.csv")
expression = pd.read_csv("expression.csv")
metadata = pd.read_csv("metadata.csv")


# In[3]:


# Displaying the dimension of the chronos dataset
chronos.shape
# Displayinng the unique values in the dataset
chrons_sampleids = chronos['Sample_ID'].unique()
len(chrons_sampleids)
# Displaying the unique gene samples
chronos_genes = list(chronos.columns)[1:]
len(chronos_genes)
# Displaying the chronos dataset
chronos.head()
# Displaying the dimesion of the cn dataset
cn.shape
# Displayinng the unique values in the dataset
cn_sampleids = list(cn['Sample_ID'].unique())
len(cn_sampleids)
# Displaying the unique gene samples
cn_genes = list(cn.columns)[1:]
len(cn_genes)
# Displaying the cn dataset
cn.head()
# Displaying the dimesion of the expression dataset
expression.shape
# Displayinng the unique values in the dataset
expression_sampleids = list(expression['Sample_ID'].unique())
len(expression_sampleids)
# Displaying the unique gene samples
expression_genes = list(expression.columns)[1:]
len(expression_genes)
# Displaying the expression dataset
expression.head()
# Displaying the dimesion of the metadata dataset
metadata.shape
# Displayinng the unique values in the dataset
metadata_sampleids = list(metadata['Sample_ID'].unique())
len(metadata_sampleids)
# Displaying the unique gene samples
metadata_genes = list(metadata.columns)[1:]
len(metadata_genes)
# Displaying the metadata dataset
metadata.head()


# In[20]:


import dash
from dash import Output, Input, Dash
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
from dash import dash_table
# from dash_table import DataTable 


# In[360]:


app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

colors = {
    'background' : '#FFFFFF',
    'text' : '#7FDFF' 
}

dataframe = {'chronos' : chronos.head(20),
             'cn' : cn.head(20), 
             'expression' : expression.head(20), 
             'metadata' : metadata.head(20)}


# In[361]:


def header():
    return html.Div(style = {'backgroundColor' : '#FFFCD',
                            'width' : '1365px',
                            'textAlign' : 'center',
                            'box-shadow' : '0 4px 8px 0 rgba(0, 0, 0, 0.4)',
                            'border' : '2px solid black',
                            "box-sizing" : "border-box",
                            'height' : '60px',
                            'display' : 'flex'
                            },
                 children = [
                       # Header
                       html.Div(style = {
                           "flex" : "17%",
                           "color" : "#D3D0CBFF",
                           "backgroundColor" : "#6E8898FF",
                           "text-align" : "left",
                           "padding" : "10px",
                           "box-sizing" : "border-box",
                           "font-weight" : "bold",
                           "font-size" : "large"
                       },
                           children = [
                           "GeneData"
                       ]),
                       html.Div(style = {"flex" : "7%"}),
                       html.Div(style = {
                           "flex" : "76%",
                           "color" : "#D3D0CBFF",
                           "backgroundColor" : "#FFFCD",
                           "text-align" : "left",
                           "padding" : "5px",
                           "box-sizing" : "border-box"
                       },
                           children = [
                           "Data Overview"
                       ])
                   ])


# In[362]:


def title_menu():
    white_button_style = {'background-color': '#9FB1BCFF',
                      'color': '#D3D0CBFF',
                      'height': '50px',
                      'width': '100%',
                      'padding-left' : '50px',
                      'text-align' : 'left',
                      "font-weight" : "bolder",
                      "border" : "none"}

    red_button_style = {'background-color': '#6E8898FF',
                        'color': '#D3D0CBFF',
                        'height': '50px',
                        'width': '100%',
                        "font-weight" : "bolder",
                        'text-align' : 'left',
                        "font-weight" : "bolder",
                        'padding-left' : '50px',
                        "border" : "none"}

    return html.Div(style = {
                  'backgroundColor' : '#2E5266FF',
                  'flex' : '17%',
                  'height' : '600px',
                  'textAlign' : 'center',
                  'box-shadow' : '0 4px 8px 0 rgba(0, 0, 0, 0.4)',
#                   'border' : "1px solid black",
                  "padding-top" : "30px",
                  "box-sizing" : "border-box",
                  
              },
              children = [
                  html.Div([
                              html.Div(
                                  children = [
                                      
                                      html.Button(id='dashboard-button',
                                                    children=['Dashboard Home'],
                                                    n_clicks=0,
                                                    style=red_button_style
                                      )
                                  ]
                              )
                              
                  ]
                  ),
                  html.Div(
                      [
                          html.Button(id='data-overview-button',
                                    children=['Data Overview'],
                                    n_clicks=0,
                                    style=white_button_style
                        )
                      ]
                  ),
                  html.Div(
                      [
                          html.Button(id='data-visualization-button',
                                    children=['Data Visualization'],
                                    n_clicks=0,
                                    style=white_button_style
                        )
                      ]
                  )
              ]
          )


# In[363]:


def home_page():
    return html.Div(style = {
        'padding' : "150px 100px 100px 100px",
        'text-align' : 'center',
        'color' : '#D3D0CBFF'
    },
        children = [
        html.H1("Welcome To Gene Data App"),
        html.H3("This App gives basic overview and visualization of gene datasets"),
        html.Br(),
        html.H5("The App gives information on chronos, cn, expression and metadata datasets"),
        html.H5("The datasets contain information on 100 genes of 908 Sample Ids")
    ])


# In[364]:


def show_data_overview_page():
    return html.Div(style = {'margin' : '30px 30px 30px 30px',
                             'border' : "1px solid black"},
                              children = [
                                          html.Div(
                                              style = {
                                                  'backgroundColor' : '#00000',
                                                  'float' : 'left',
                                                  'width' : '17.5%',
                                                  'height' : '500px',
                                                  'textAlign' : 'center',
                                                  'box-shadow' : '0 4px 8px 0 rgba(0, 0, 0, 0.4)',
                                                  'padding' : '1%',
                                                  'border' : "1px solid black"
                                              },
                                              children = [
                                                  html.Div(style = {'color' : '#73A5C6',
                                                                    'font-weight' : 'bold',
                                                                    'text-align' : 'left',
                                                                    'border' : "1px solid black"
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
                                              ]
                                          ),
                                          html.Div(style = {'width' : '2%'}),
                                          html.Div(
                                          style = {
                                              'overflowY' : 'scroll',
                                              'padding' : '1%',
                                              'border' : '2px solid black',
                                              'float' : 'right',
                                              'width' : '47.5%',
                                              'backgroundColor' : '#00000',
                                              'box-shadow' : '0 4px 8px 0 rgba(0, 0, 0, 0.4)',
                                              'textAlign' : 'center',
                                              'maxHeight' : '500px',
                                              'border' : "1px solid black"
                                          },
                                          children = [
                                              html.Div(id = "table")
                                          ]
                                      ),
                                        html.Div([dbc.Alert(id ="tbl_out")]),
                                        html.Div(style = {'clear' : 'right'})
                              ]
                          )


# In[366]:


def draw_scatter_plot():
    return html.Div(style = {'width' :'50%',
                             'float' : 'left'},
             children = [
                         html.Div(
                        style = {
                            'padding' : '20px',
                            'margin' : '20px 20px 20px 20px',
                            'box-shadow' : '0 4px 8px 0 rgba(0, 0, 0, 0.4)',
                            'textAlign' : 'left',
                            'box-sizing' : 'border-box'

                        },
                        children = [
                            dbc.Row([
                                dbc.Col(
                                    [
                                    html.Div(
                                        [
                                            html.H6("Select Chronos Field"),
                                            dcc.Dropdown(style = {"width" : "150px"},
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
                                dbc.Col(
                                    [
                                    html.Div(
                                        [
                                            html.H6("Select Expression Field"),
                                            dcc.Dropdown(style = {"width" : "150px"},
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
                                dbc.Col([
                                    html.Div(
                                        [
                                            html.H6("Select metadata Field"),
                                            dcc.Dropdown(style = {"width" : "150px"},
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
                    )
                    ,
                    html.Div( style = {
                                        'padding' : '20px 20px 20px 20px',
                                        'margin' : '20px 20px 20px 20px',
                                        'box-shadow' : '0 4px 8px 0 rgba(0, 0, 0, 0.4)',
                                        'textAlign' : 'center',
                                        'box-sizing' : 'border-box',
                    },
                        children = [
                            html.Div(style = {
                                                'padding' : '10px 10px 10px 10px',
                                                'box-shadow' : '0 4px 8px 0 rgba(0, 0, 0, 0.4)',
                                                'textAlign' : 'center',
                                                'box-sizing' : 'border-box'
                                            },
                                children = [
                                        dbc.Row(
                                            [
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


# In[367]:


def draw_violin_plot():
    return html.Div(style = {"flex" : "50%"
                            },
             children = [
                         html.Div(
                         style = {
                            'padding' : '20px',
                            'margin' : '20px 20px 20px 20px',
                            'box-shadow' : '0 4px 8px 0 rgba(0, 0, 0, 0.4)',
                            'textAlign' : 'left',
                            'box-sizing' : 'border-box'

                        },
                        children = [
                            dbc.Row([
                                dbc.Col(
                                    [
                                    html.Div(
                                        [
                                            html.H6("Select Gene"),
                                            dcc.Dropdown(style = {"width" : "150px"},
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
                                dbc.Col(
                                    [
                                    html.Div(
                                        [
                                            html.H6("Select Dataset"),
                                            dcc.Dropdown(style = {"width" : "150px"},
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
                                dbc.Col([
                                    html.Div(
                                        [
                                            html.H6("Select Metadata Field"),
                                            dcc.Dropdown(style = {"width" : "150px"},
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
                    )
                    ,
                    html.Div( style = {
                                        'padding' : '20px 20px 20px 20px',
                                        'margin' : '20px 20px 20px 20px',
                                        'box-shadow' : '0 4px 8px 0 rgba(0, 0, 0, 0.4)',
                                        'textAlign' : 'center',
                                        'box-sizing' : 'border-box',
                    },
                        children = [
                            html.Div(style = {
                                                'padding' : '10px 10px 10px 10px',
                                                'box-shadow' : '0 4px 8px 0 rgba(0, 0, 0, 0.4)',
                                                'textAlign' : 'center',
                                                'box-sizing' : 'border-box'
                                            },
                                children = [
                                        dbc.Row(
                                            [
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


# In[368]:


def draw_plots():
       return html.Div(style = {
        'margin' : '30px 30px 30px 30px',
        'padding' : '20px 20px 20px 20px',
        'box-shadow' : '0 4px 8px 0 rgba(0, 0, 0, 0.4)',
        'textAlign' : 'center',
        'box-sizing' : 'border-box',
        "display" : "flex"
    },
        children = [
            draw_scatter_plot(),
            draw_violin_plot(),
        ]

    )


# In[369]:


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
        return show_data_overview_page()
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


# In[370]:


if __name__ == '__main__':
    app.run_server(debug = True, use_reloader = False)


# In[94]:


app.layout = html.Div(style = {'backgroundColor' : colors['background']}, 
                      children = [
                          html.Div(style = {'backgroundColor' : '#FFFCD',
                                            'width' : '1323px',
                                            'textAlign' : 'center',
                                            'box-shadow' : '0 4px 8px 0 rgba(0, 0, 0, 0.4)',
                                            'border' : '2px solid black',
                                            "padding" : "5px",
                                            "box-sizing" : "border-box",
                                            'height' : '50px',
                                            'display' : 'flex'
                                            }, 
                                   children = [
                                       # Header
                                       html.Div(style = {
                                           "flex" : "20%",
                                           "color" : "#FFFFFF",
                                           "backgroundColor" : "#73A5C6",
                                           "text-align" : "left",
                                           "padding" : "5px",
                                           "box-sizing" : "border-box"
                                       },
                                           children = [
                                           "GeneData"
                                       ]),
                                       html.Div(style = {
                                           "flex" : "80%",
                                           "color" : "#00000",
                                           "backgroundColor" : "#FFFCD",
                                           "text-align" : "left",
                                           "padding" : "5px",
                                           "box-sizing" : "border-box"
                                       },
                                           children = [
                                           "Data Overview"
                                       ])
                                   ]
                          ),
                          html.Div(style = {'height' : '1px'
                                           }),
                          # Filter dropdown
                          html.Div(style = {'margin' : '30px 30px 30px 30px',
                                            'border' : "1px solid black"},
                              children = [
                                  html.Div(
                                      style = {
                                          'backgroundColor' : '#00000',
                                          'float' : 'left',
                                          'width' : '17.5%',
                                          'height' : '500px',
                                          'textAlign' : 'center',
                                          'box-shadow' : '0 4px 8px 0 rgba(0, 0, 0, 0.4)',
                                          'padding' : '1%',
                                          'border' : "1px solid black"
                                      },
                                      children = [
                                          html.Div(style = {'color' : '#73A5C6',
                                                            'font-weight' : 'bold',
                                                            'text-align' : 'left',
                                                            'border' : "1px solid black"
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
                                      ]
                                  ),
                                  html.Div(style = {'width' : '2%'}),
                                  html.Div(
                                  style = {
                                      'overflowY' : 'scroll',
                                      'padding' : '1%',
                                      'border' : '2px solid black',
                                      'float' : 'right',
                                      'width' : '47.5%',
                                      'backgroundColor' : '#00000',
                                      'box-shadow' : '0 4px 8px 0 rgba(0, 0, 0, 0.4)',
                                      'textAlign' : 'center',
                                      'maxHeight' : '500px',
                                      'border' : "1px solid black"
                                  },
                                  children = [
                                      html.Div(id = "table")
                                  ]
                              ),
                                html.Div([dbc.Alert(id ="tbl_out")]),
                                html.Div(style = {'clear' : 'right'})
                              ]
                          )
             ])

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
#     return 'You have selected "{}"'.format(dataframe[value])

# @app.callback(
#     Output("update-summary-statics", "children"), [Input("change-table", "value")]
# )
# def update_summary_statics(value):
#     return html.Div(
#                     ['Number Of Rows : {}'.format(dataframe[value].shape[0]), 
#                       html.Br(),
#                      'Number Of columns : {}'.format(dataframe[value].shape[1])]
#                    )                             
# @app.callback(
#     Output("tbl_out", "children"), Input("table", "active_cell")
# )
# def update_graphs(active_cell):
#     return str(active_cell) if active_cell else "Click the table"


# In[95]:


if __name__ == '__main__':
    app.run_server(debug = True, use_reloader = False)


# In[ ]:


html.Div(style = {'width': '100%',
                 'height' : '100%',
                 'backgroundColor' : '#FFFCD',
                 'border' : '2px solid black',
                 },
        children = [
            dbc.Row([
                        dbc.Col([
                            html.Div('Gene Datasets')
                        ]),
                        dbc.Col([
                            html.Div('Data Overview')
                        ])
            ])
        ]
        )


# In[ ]:


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


# In[ ]:


children =[
                                      html.Div(style = {"flex" : "25%"},
                                               children =[html.Img(src=app.get_asset_url('home.jpg'), style={'height':'100%', 'width':'100%'})]),
                                      html.Div(style = {"flex" : "75%"},
                                          children = [
                                              html.Button(id='dashboard-button',
                                                        children=['Dashboard'],
                                                        n_clicks=0,
                                                        style=white_button_style
                                                )
                                      ])
                                      
                                  ]

