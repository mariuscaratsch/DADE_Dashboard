import pandas as pd
import plotly.express as px
import numpy as np

Daten auslesen
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

display(df)