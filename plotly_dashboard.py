# Was noch nicht funktioniert:

# - Filter Lebenserwartun gChart 4
# - Filter Höhe und durchschnittliche Anzahl Blätter Chart 3
# - Filter Klima, höhe und Lebenserwartung in Chart einbauen

### ----- Imports ----- ###

# Datenset bearbeiten
import pandas as pd

# Diagramme erstellen
import plotly.express as px

# Dashbaord erstellen
from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

# Schriftart laden
external_stylesheets = [
    "'https://fonts.googleapis.com/css2?family=Caveat:wght@400;500;600;700&display=swap'"]


### ----- Methoden ----- ###

# Zählt die Anzahl an Farben
def get_color_count(color, dff):
    values = dff["Farbe"].value_counts()[color]
    return values


def get_unique_flower_colors(df):
    colors = df["Farbe"].unique()
    return colors

# Holt die Kontinente
def get_continents(df):
    continent = df["Herkunftskontinent"].unique()
    return continent


def get_heights(df):
    heights = df["Höhe"].unique()
    return heights


def get_life_expectancies(df):
    expectancies = df["Lebenserwartung_numeric"].unique()
    return expectancies

# Gibt einen Durchschnittswert der Lebenserwartung zurück (wegen Datensatz)


def get_expectancy_numeric(expectancy_str):
    match expectancy_str:
        case "1-2":
            return 1.5
        case "2-3":
            return 2.5
        case "5-10":
            return 7.5

# Holt die durchschinttliche Lebenserwartung


def get_continent_expectancy_count(continent, dff):
    result = dff[dff["Herkunftskontinent"] == continent]
    avg = result["Lebenserwartung_numeric"].mean()
    return avg


def get_climates(df):
    return list(df["Klima"].unique())

### ----- Daten einlesen ----- ###


# CSV Datei wird geladen
df = pd.read_csv('flower_data.csv')

# Dictionary welches die  Namen der Spalten mit den neuen Name (Deutsch) verknüpft.
dict = {'name': 'Name',
        'height (cm)': 'Höhe',
        'longevity (years)': 'Lebenserwartung',
        'place of origin': 'Herkunftskontinent',
        'color': 'Farbe',
        'climate': 'Klima',
        'cut flowers': 'Geschnittene Blume',
        'perfumes': 'Parfum',
        'medicine': 'Medizin',
        'average number of petals': 'Durchschnittliche Anzahl Blätter'}

corrected_climates = {
    "Temperate": "Temperate",
    "Temperate to tropical": "Temperate to Tropical",
    "Tropical": "Tropical",
    "Tropical to temperate": "Temperate to Tropical",
    "Desert": "Desert",
    "cold": "Cold",
    "temparate": "Temperate",
    "temperate": "Temperate"
}


# Umbenennung der Spalten mithilfe des Dictionaries (Änderungen werden direkt auf das DataFrame angewendet)
df.rename(columns=dict, inplace=True)
df["Herkunftskontinent"] = df["Herkunftskontinent"].str.split(", ")
df = df.explode("Herkunftskontinent")
df["Klima"] = df["Klima"].str.split(", ")
df = df.explode("Klima")
df["Klima"] = df["Klima"].replace(corrected_climates)

df["Lebenserwartung_numeric"] = df.apply(
    lambda x: get_expectancy_numeric(x["Lebenserwartung"]), axis=1)
flower_colors = get_unique_flower_colors(df)
continents = get_continents(df)
heights = get_heights(df)
expectancies = get_life_expectancies(df)
climates = get_climates(df)
marks = {}
for index, climate in enumerate(climates):
    marks[index] = {'label': climate}

# Startet die Dashboard App
app = Dash(title="Bluemenwelten - The Dashboard",
           external_stylesheets=[dbc.themes.BOOTSTRAP])

server=app.server

### ----- Statische Diagramme (ohne callback) ----- ###

# Balkendiagramm horizontal welches die Lebenserwartung der Blumen nach Herkunftskontinent anzeigt
def create_bar_chart():

    # /// Schnitt der Lebenserwartung pro Kontinent berechnen
    dff = df.copy()
    dff["Herkunftskontinent"] = dff["Herkunftskontinent"].str.split(", ")

    bar_chart_fig = px.bar(dff, x="Lebenserwartung",
                           y="Herkunftskontinent", orientation='h')
    return bar_chart_fig


### ----- Layout ----- ###

app.layout = html.Div(
    children=[

        # Titel des Dashboards
        dbc.Row([
                dbc.Col([
                    html.H1("Bluemenwelten - The Dashboard"),
                ], width=12, className=""),
                ], className="title_wrapper"),

        # Content des Dashboards
        dbc.Row([

                # Filter Bereich (links) des Dashboards
                dbc.Col([
                    html.H2("Filter"),

                    # First row
                    dbc.Row([

                        # Auswahl der Blume/-n
                        dbc.Col([
                            html.H3("Blumenart"),
                            dcc.Checklist(id='choose-flowers', options=['Rose', 'Tulip', 'Daisy', 'Sunflower', 'Orchid', 'Jasmine', 'Lavender', 'Marigold', 'Chrysanthemum', 'Daffodil', 'Freesia', 'Iris', 'Lily', 'Peony', 'Gardenia', 'Gladiolus', 'Hyacinth', 'Lilac', 'Narcissus', 'Poppy', 'Snapdragon', 'Violet', 'Zinnia', 'Alstroemeria', 'Anemone', 'Asters', 'Calendula', 'Carnation', 'Cosmos', 'Dandelion', 'Delphinium', 'Foxglove', 'Ylang-ylang', 'Tuberose', 'Honeysuckle', 'Frangipani', 'Heliotrope', 'Geranium',
                                          'Clove', 'Cumin', 'Cactus', 'Venus flytrap', 'Pitcher plant', 'Sundew', 'Bladderwort', 'Butterwort', 'Cobra lily', 'Cobra plant', 'Corkscrew plant', 'Larkspur', 'Monkshood', 'Digitalis', 'Echinops', 'Hollyhock', 'Verbena', 'Violets', 'Pansies', 'Johnny jump ups', 'Violas', 'Forget-me-nots', 'Sweet Williams', 'Primroses', 'Cyclamen', 'Dwarf iris', 'Bluebell', 'Daffodil', 'Crocus', 'Hyacinth', 'Iris reticulata', 'Chionodoxa', 'Anemone', 'Scilla'], className="checklist_content"),
                        ], className="filter_instance_wrapper"),


                        dbc.Col([

                            # Auswahl der Farbe/-n
                            html.Div([
                                html.H3("Farbe"),
                                dcc.Checklist(id='choose-colors',
                                              options=flower_colors)
                            ], className="filter_instance_wrapper_secondary after wrapper_padding-bottom"),

                            # Auswahl der Grössee/-n
                            html.Div([
                                html.H3("Höhe"),
                                dcc.Dropdown(id='choose-height', options=heights, multi=True, value=heights, className="filter_instance_wrapper_secondary after")]),

                            # Auswahl der Lebenserwartung/-en
                            html.Div([
                                html.H3("Lebenserwartung"),
                                dcc.Dropdown(
                                    id='choose-life-expectancy', options=expectancies, multi=True, value=expectancies),
                            ], className="filter_instance_wrapper_secondary wrapper_padding-bottom"),
                        ]),
                    ], className="margin_bottom"),

                    # Second Row
                    dbc.Row([
                            dbc.Col([
                                html.H3("Klima"),
                                dcc.Slider(id='choose-climate', value=0, min=0, max=len(climates)-1, step=1,
                                           marks=marks),
                            ], className="filter_instance_wrapper_secondary margin_right wrapper_padding-bottom"),
                            ], className="wrapper_padding-bottom"),
                    # Second Row
                    dbc.Row([
                            dbc.Col([
                                html.H3("Kontinent"),
                                dcc.Dropdown(id='choose-continent',
                                             options=continents, multi=True),
                            ], className="filter_instance_wrapper_secondary margin_right wrapper_padding-bottom"),
                            ], className=""),
                ], className="filter_wrapper", width=4),



                # Diagrammbereich (rechts) des Dashboards
                dbc.Col([
                    html.H2("Diagramme"),

                    # Erste Reihe mit zwei Diagrammen
                    dbc.Row([
                        dbc.Col([
                            html.Div([
                                html.H3("Anzahl Blumen nach Farbe"),
                                dbc.Badge("Filter Blumenart", color="primary", style={
                                          "marginRight": "1rem"}),
                                dbc.Badge("Filter Farbe", color="primary", style={
                                          "marginRight": "1rem"}),
                                # Balkendiagramm
                                dcc.Graph(
                                    id='graph-bar-chart-output', figure={})
                            ], className="chart_instance_wrapper wrapper_padding-bottom"),
                        ], width=12),
                        # dbc.Col([
                        # html.Div([
                        # html.H3("Herkunft der Blumenart"),
                        # Karte
                        # dcc.Graph(id='graph-map-output', figure={})
                        # ], className="chart_instance_wrapper wrapper_padding-bottom"),
                        # ], width=6),
                    ], className="after"),

                    # Zweite Reihe mit drei Diagrammen
                    dbc.Row([
                        dbc.Col([
                            html.Div([
                                html.H3("Blumen nach Herkunftskontinent"),
                                # Kreisdiagramm
                                dbc.Badge("Filter Kontinent", color="primary", style={
                                          "marginRight": "1rem"}),
                                dcc.Graph(id="pie-chart"),
                            ], className="chart_instance_wrapper wrapper_padding-bottom"),
                        ], lg=4),
                        dbc.Col([
                            html.Div([
                                html.H3("Höhe der Blumen und Blätter"),
                                # Scatter
                                dbc.Badge("Filter Höhe", color="primary", style={
                                          "marginRight": "1rem"}),
                                dcc.Graph(id="scatter-chart-output", figure={})
                            ], className="chart_instance_wrapper wrapper_padding-bottom"),
                        ], lg=4),
                        dbc.Col([
                            html.Div([
                                html.H3("Lebenserwartung nach Kontinent"),
                                dbc.Badge("Filter Lebenserwartung", color="primary", style={
                                          "marginRight": "1rem"}),
                                dbc.Badge("Filter Klima", color="primary", style={
                                          "marginRight": "1rem"}),
                                dbc.Badge("Filter Kontinent", color="primary", style={
                                          "marginRight": "1rem"}),
                                # Balkendiagramm mit horizontal
                                dcc.Graph(id='bar_chart_fig')
                            ], className="chart_instance_wrapper wrapper_padding-bottom"),
                        ], lg=4),
                    ]),
                ], className="chart_wrapper", width=8)
                ], className="content_wrapper"),
    ], className="frame")


### ----- Diagramme ----- ###

# Balkendiagramm vertikal Anzahl der Blumen pro jeweiliger Farbe graph-bar-chart-output
@app.callback(
    Output('graph-bar-chart-output', 'figure'),
    Input('choose-flowers', 'value'),
    Input('choose-colors', 'value'))
def update_graph_bar_chart(flower_names, flower_colors):
    dff = df.copy()
    if flower_names != None and len(flower_names) > 0:
        dff = dff[dff["Name"].isin(flower_names)]

    if flower_colors != None and len(flower_colors) > 0:
        dff = dff[dff["Farbe"].isin(flower_colors)]

    dff_bar_chart = pd.DataFrame()
    dff_bar_chart["Farbe"] = dff["Farbe"].unique()
    dff_bar_chart["Anzahl"] = dff_bar_chart.apply(
        lambda x: get_color_count(x["Farbe"], dff), axis=1)
    fig = px.bar(dff_bar_chart, x="Farbe", y="Anzahl")
    return fig

# Karte mit den Herkunftskontinenten der Blumen
# Die Karte muss leider aus dem Dashbard entfernt werden, da es keine Möglichkeit gab die Kontinente zu markieren

# @app.callback (
    # Output(component_id='graph-map-output', component_property='figure'),
    # Input(component_id='choose-flowers', component_property='value'),

    # Beim Laden des Dashboards wird der callback nicht getriggert
    # prevent_initil_call=True
    # )

# def update_graph_map(val_chosen):

    # print(f" user chose: {val_chosen}")
    # fig = go.Figure(go.Scattergeo())
    # fig.update_layout(height=300, margin={"r":0,"t":0,"l":0,"b":0})
    # return fig

# Kreisdriagramm pie-chart


@app.callback(Output("pie-chart", "figure"),
              Input("choose-continent", "value"))
def update_pie_chart(continents):
    dff = df.copy()
    if continents != None and len(continents) > 0:
        dff = dff[dff["Herkunftskontinent"].isin(continents)]

    origin_counts = dff["Herkunftskontinent"].value_counts()
    pie_chart_fig = px.pie(values=origin_counts,
                           names=origin_counts.index, hole=0)
    return pie_chart_fig

# Scatter Diagramm welches die Höhe und Anzahl von Blättern einer Pflanze anzeigt scatter-chart-output


@ app.callback(
    Output('scatter-chart-output', 'figure'),
    Input('choose-height', 'value')
)
def update_graph_scatter(height_category):
    dff = df.copy()
    if height_category != None and len(height_category) > 0:
        dff = dff[dff["Höhe"].isin(height_category)]
    fig = px.scatter(dff, x="Durchschnittliche Anzahl Blätter", y="Höhe")
    return fig

# Balkendiagramm das die Lebenserwartung in Bezug zum Herkunftskontinent anzeigt bar_chart_fig


@app.callback(
    Output('bar_chart_fig', 'figure'),
    Input('choose-continent', 'value'),
    Input('choose-life-expectancy', 'value'),
    Input('choose-flowers', 'value'),
    Input('choose-climate', 'value'))
def update_bar_chart_fig(continents, life_expectancies, flower_names, climate_number):
    climate = marks[climate_number]['label']
    dff = df.copy()
    if continents != None and len(continents) > 0:
        dff = dff[dff["Herkunftskontinent"].isin(continents)]

    if flower_names != None and len(flower_names) > 0:
        dff = dff[dff["Name"].isin(flower_names)]

    if life_expectancies != None and len(life_expectancies) > 0:
        dff = dff[dff["Lebenserwartung_numeric"].isin(life_expectancies)]

    dff = dff[dff["Klima"] == climate]

    fig = px.bar(dff, y="Lebenserwartung_numeric", x="Name",
                 barmode="group", color="Herkunftskontinent")
    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
