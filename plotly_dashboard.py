import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc, callback
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import numpy as np

### Load Font
external_stylesheets = ["'https://fonts.googleapis.com/css2?family=Caveat:wght@400;500;600;700&display=swap'"]

### Load Data
df = pd.read_csv('flower_data.csv')

dict = {'name': 'Name',
        'height (cm)': 'Höhe',
        'longevity (years)': 'Lebenserwartung',
        'place of origin': 'Herkunftskontinent',
        'color': 'Farbe',
        'climate': 'Klima',
        'cut flowers': 'Geschnittene Blume',
        'perfumes': 'Parfum',
        'medicine': 'Medizin',
        'average number of petals': 'Durchschnittliche Anzhal Blätter'}

df.rename(columns=dict, inplace=True)

### Charts


### Widgets


### Layout

app = Dash(title="Bluemenwelten - The Dashboard", external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div(
    children=[
            
        ### Titel des Dashboards
        dbc.Row ([
                dbc.Col ([
                        html.H1("Bluemenwelten - The Dashboard"),
                ], width=12, className=""),
        ], className="title_wrapper"),

        ### Content des Dashboards
        dbc.Row ([

                ### Filter Bereich (links) des Dashboards
                dbc.Col([
                        html.H2("Filter"),
                        
                        ### First row
                        dbc.Row([

                                ### Auswahl der Blume/-n
                                dbc.Col([
                                        html.H3("Blumenart"),
                                        dcc.Checklist(['Rose', 'Tulip', 'Daisy', 'Sunflower', 'Orchid', 'Jasmine', 'Lavender', 'Marigold', 'Chrysanthemum', 'Daffodil', 'Freesia', 'Iris', 'Lily', 'Peony', 'Gardenia', 'Gladiolus', 'Hyacinth', 'Lilac', 'Narcissus', 'Poppy', 'Snapdragon', 'Violet', 'Zinnia', 'Alstroemeria', 'Anemone', 'Asters', 'Calendula', 'Carnation', 'Cosmos', 'Dandelion', 'Delphinium', 'Foxglove', 'Ylang-ylang', 'Tuberose', 'Honeysuckle', 'Frangipani', 'Heliotrope', 'Geranium', 'Clove', 'Cumin', 'Cactus', 'Venus flytrap', 'Pitcher plant', 'Sundew', 'Bladderwort', 'Butterwort', 'Cobra lily', 'Cobra plant', 'Corkscrew plant', 'Larkspur', 'Monkshood', 'Digitalis', 'Echinops', 'Hollyhock', 'Verbena', 'Violets', 'Pansies', 'Johnny jump ups', 'Violas', 'Forget-me-nots', 'Sweet Williams', 'Primroses', 'Cyclamen', 'Dwarf iris', 'Bluebell', 'Daffodil', 'Crocus', 'Hyacinth', 'Iris reticulata', 'Chionodoxa', 'Anemone', 'Scilla'], className="checklist_content"),
                                ], className="filter_instance_wrapper"),


                                dbc.Col([

                                        ### Auswahl der Farbe/-n
                                        html.Div([
                                                        html.H3("Farbe"),
                                                        dcc.Checklist(['Weiss', 'Gelb', 'Rot', 'Lila', 'Rosa', 'Blau']) 
                                        ], className="filter_instance_wrapper_secondary after"),

                                        ### Auswahl der Grössee/-n
                                        html.Div([
                                                        html.H3("Höhe"),
                                                        dcc.Checklist(
                                                                [
                                                                        {
                                                                        "label": [
                                                                                html.Img(src="/assets/images/flower.png", style={"height": 20}),
                                                                                html.Span("10-29", style={"font-size": 15, "padding-left": 10}),
                                                                        ],
                                                                        "value": "10-29",
                                                                        },
                                                                        {
                                                                        "label": [
                                                                                html.Img(src="/assets/images/flower.png", style={"height": 40}),
                                                                                html.Span("30-69", style={"font-size": 15, "padding-left": 10}),
                                                                        ],
                                                                        "value": "30-69",
                                                                        },
                                                                        {
                                                                        "label": [
                                                                                html.Img(src="/assets/images/flower.png", style={"height": 60}),
                                                                                html.Span("70-100", style={"font-size": 15, "padding-left": 10,"display": "flex"}),
                                                                        ],
                                                                        "value": "70-100",
                                                                        },
                                                                ],
                                                                labelStyle={"display": "flex", "align-items": "center"},
                                                        )  
                                        ], className="filter_instance_wrapper_secondary wrapper_padding-bottom after"),

                                        ### Asuwahl der Lebenserwartung/-en
                                        html.Div([
                                                        html.H3("Lebenserwartung"),
                                                        dcc.Dropdown(['1-2', '2-3', '5-10'], '1-2', id='lebenserwartung-dropdown'),
                                        ], className="filter_instance_wrapper_secondary wrapper_padding-bottom"),
                                ]),
                        ], className="margin_bottom"),

                        ### Second Row
                        dbc.Row([
                                dbc.Col([
                                        html.H3("Klima"),
                                        dcc.Slider(0, 100, step=33,
                                                marks={
                                                        0: {'label': 'kalt'},
                                                        33: {'label': 'gemässigt'},
                                                        66: {'label': 'trpoisch'},
                                                        100: {'label': 'Wüste'}
                                                }
                                        ),
                                ], className="filter_instance_wrapper_secondary margin_right"),
                        ]),
                ], className="filter_wrapper", width=4),

                ### Filterbereich (rechts) des Dashboards
                dbc.Col([
                        html.H2("Diagramme"),
                        html.Div("Diagramme Inhalte"),
                ], className="chart_wrapper", width=8)
        ], className="content_wrapper"),
    ], className="frame")

if __name__ == "__main__":
        app.run_server(debug=True)