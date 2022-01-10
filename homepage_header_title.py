#!/usr/bin/env python
# coding: utf-8

# ## HomePage - header - title 

# - This page gives the functions for the header, title menu and the home page in the app 

# In[6]:


from dash import html 
import dash


# ### Function to plot the header layout

# In[7]:


def header():
    '''
    This function gives the header of the layout in the app
    param : none
    return html Div which contains the layout of the header in the app 
    '''
    # specify the style of the layout of the header
    return html.Div(style = {'backgroundColor' : '#FFFCD',
                            'width' : '1365px',
                            'textAlign' : 'center',
                            'box-shadow' : '0 4px 8px 0 rgba(0, 0, 0, 0.4)',
                            'border' : '2px solid black',
                            "box-sizing" : "border-box",
                            'height' : '60px',
                            'display' : 'flex'
                            },
                 # # Specify the style for the app name
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
                           "font-size" : "150%"
                       },
                           # Display the name of the gene app 
                           children = [
                           "GeneData"
                       ]),
                       html.Div(style = {"flex" : "1%"}),
                       # Specify the style of the name of the page in the app layout
                       html.Div(style = {
                           "flex" : "82%",
                           "color" : "#D3D0CBFF",
                           "backgroundColor" : "#FFFCD",
                           "text-align" : "left",
                           "padding" : "13px",
                           "box-sizing" : "border-box",
                           
                       },
                           # Display the name of the page displayed in the app
                           
                           id = "layout-page-title"
                     )
                   ])


# ### Function to plot the title layout

# In[ ]:


def title_menu():
    '''
    This function gives the title menu of the layout in the app
    param : none
    return html Div which contains the layout of the title in the app 
    '''
    # specify the style of the color of the button which is unpressed
    white_button_style = {'background-color': '#9FB1BCFF',
                      'color': '#D3D0CBFF',
                      'height': '50px',
                      'width': '100%',
                      'padding-left' : '50px',
                      'text-align' : 'left',
                      "font-weight" : "bolder",
                      "border" : "none"}
    
    # specify the style of the color of the button which is pressed
    red_button_style = {'background-color': '#6E8898FF',
                        'color': '#D3D0CBFF',
                        'height': '50px',
                        'width': '100%',
                        "font-weight" : "bolder",
                        'text-align' : 'left',
                        "font-weight" : "bolder",
                        'padding-left' : '50px',
                        "border" : "none"}
    
    # Specify the style of the title buttons in the title layout
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
                    
              # display the button for the dashboard home in the title layout in the app 
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
                  # Display the button for the data overview in the title of the app
                  html.Div(
                      [
                          html.Button(id='data-overview-button',
                                    children=['Data Overview'],
                                    n_clicks=0,
                                    style=white_button_style
                        )
                      ]
                  ),
                  # Display the button for the data visualization in the title of the app
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


# ### Function to plot the home page layout

# In[ ]:


def home_page():
    '''
    This function gives the home page of the layout in the app
    param : none
    return : html Div which contains the layout of the home page in the app 
    '''
    # Specify the style for the home page layout
    return html.Div(style = {
        'padding' : "150px 100px 100px 100px",
        'text-align' : 'center',
        'color' : '#D3D0CBFF',
        'background-image': 'url(C://Users//nithin//Desktop//EucildataAssignment//ElucidataAssignment//homepagebackground.jpg)',
        'opacity' : '0.5'
    },
        # Display the home page text
        children = [
        html.H1("Welcome To Gene Data App"),
        html.H3("This App gives basic overview and visualization of gene datasets"),
        html.Br(),
        html.H5("The App gives information on chronos, cn, expression and metadata datasets"),
        html.H5("The datasets contain information on 100 genes of 908 Sample Ids")
    ])

