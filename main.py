import pandas as pd
import numpy as np
import plotly.express as px

# Criando um DataFrame com dados simulados
data = pd.DataFrame({
    'latitude': [-23.5505, 48.8566, 34.0522],               # São Paulo, Paris, Los Angeles
    'longitude': [-46.6333, 2.3522, -118.2437],
    'location_latitude': [-22.9068, 51.5074, 40.7128],      # Rio de Janeiro, Londres, Nova York
    'location_longitude': [-43.1729, -0.1278, -74.0060]
})

print("Dados iniciais:")
print(data.head())

data.info()

print("\nValores nulos por coluna:")
print(data.isnull().sum())

# Raio da Terra em km
R = 6371

# Função para converter graus em radianos
def deg_to_rad(degrees):
    return degrees * (np.pi / 180)

# Fórmula de Haversine
def dist(lat1, lon1, lat2, lon2):
    d_lat = deg_to_rad(lat2 - lat1)
    d_lon = deg_to_rad(lon2 - lon1)
    a = np.sin(d_lat / 2) ** 2 + np.cos(deg_to_rad(lat1)) * np.cos(deg_to_rad(lat2)) * np.sin(d_lon / 2) ** 2
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))
    return R * c

data['distance'] = data.apply(lambda row: dist(row['latitude'], row['longitude'], 
                                               row['location_latitude'], row['location_longitude']), axis=1)

print("\nDados com a coluna de distância:")
print(data)

fig = px.bar(data, x=data.index, y='distance', 
             labels={'index': 'Par de Localizações', 'distance': 'Distância (km)'},
             title='Distâncias Calculadas Entre Pontos Geográficos')
fig.show()
