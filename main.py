# filename = 'main.py'

#
# Imports
#

import dash
from dash import dcc
from dash import html

import folium, branca
import pandas as pd
import plotly.express as px

#
# Data
#


f = open('velib-disponibilite-en-temps-reel.csv', 'r', encoding='utf-8')
df = pd.read_csv(f, delimiter=";", encoding = 'utf8')

"""gapminder = px.data.gapminder() # (1)
years = gapminder["year"].unique()
data = { year:gapminder.query("year == @year") for year in years} # (2)"""

coord = df["Coordonnées géographiques"]
nb_velib = df["Nombre total vélos disponibles"]
cap_sta = df["Capacité de la station"]

l = list()
latitude = list()
longitude = list()
intermed = list()
nombre_velo = list()
capacite_station = list()
i = 0
for elt in coord :
    l.append(elt)
    intermed = l[i].split(',')
    latitude.append(intermed[0])
    longitude.append(intermed[1])
    i += 1

for elt in nb_velib :
    nombre_velo.append(elt)
    
for elt in cap_sta :
    capacite_station.append(elt)

#
# Main
#

if __name__ == '__main__':

    app = dash.Dash(__name__) # (3)

    coords = (48.856614, 2.3522219)
    map = folium.Map(location=coords, tiles='Stamen Toner', zoom_start=13)

    """fig = px.scatter(data[year], x="gdpPercap", y="lifeExp",
                        color="continent",
                        size="pop",
                        hover_name="country") # (4)"""
    cm = branca.colormap.LinearColormap(['green', 'red'], vmin=min(nombre_velo), vmax=max(nombre_velo))
    map.add_child(cm) # add this colormap on the display
    k = 0

    for lat, lng, size, color in zip(latitude, longitude, capacite_station, nombre_velo):
        folium.CircleMarker(
            location=[lat, lng],
            radius=size/5,
            color = cm(color),
            fill = True,
            fill_color = cm(color),
            fill_opacity=0.6,
            tooltip=df['Nom station'][k]
        ).add_to(map)

        k += 1

    map.save(outfile='map.html')

    fig = px.histogram(df, x=cap_sta)
    fig2 = px.histogram(df, x=nb_velib)

    app.layout = html.Div([
        html.H1("Dashboard des stations Vélib'",style={'textAlign': 'center'}),
        html.H2(id='Title1',children="Map des différentes stations d'ile de France",style={'text-align':'center'}), 
        html.Div(id='Title2', children='''
        La map représente toutes les stations de vélib d'île de France, les stations sont représentées par des points. La couleur nous montre combien de vélos sont disponibles, le vert correspond au minimum et le rouge au maximum. La taille quant à elle représente la capacité de la station : Plus elle est grande plus la capacité est importante.
        ''',style={'margin-bottom':'50px', 'text-align':'center'}),
        html.Iframe(id = 'map', srcDoc = open('map.html', 'r').read(), width = '100%', height='500'),
        html.Div([html.H1('Répartition du nombre de vélos disponibles dans les stations',style={'textAlign': 'center', 'color': '#318CE7'}),]),
        dcc.Graph(id='graph1',figure=fig2),
        html.Div('''L'histogramme ci-dessus représente le nombre de station vélib' en fonction de leur nombre de vélos disponibles. Par exemple, il y a 336 stations dans lesquelles aucun vélo n'est disponible.''',style={'textAlign': 'center', 'color': '#005C96'}),
        html.Div([html.H1('Répartition des différentes capacité de station',style={'textAlign': 'center', 'color': '#318CE7'}),]),
        dcc.Graph(id='graph2',figure=fig),
        html.Div('''L'histogramme ci-dessus représente le nombre de station vélib' en fonction de leur capacité totale. Par exemple, il y a 133 stations dont la capacité totale est de 24 ou 25 vélos.''',style={'textAlign': 'center', 'color': '#005C96'}),
        ])

    #
    # RUN APP
    #

    app.run_server(debug=True) # (8)