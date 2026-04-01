from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import math

app = FastAPI(title="Masar.AI Engine")

# Autoriser ton fichier HTML local à discuter avec ce serveur Python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_methods=["*"],
    allow_headers=["*"],
)

def calculate_distance(lat1, lon1, lat2, lon2):
    return math.sqrt((lat2 - lat1)**2 + (lon2 - lon1)**2)

@app.get("/api/route")
def generate_ai_route(theme: str):
    # 1. Charger la vraie base de données CSV
    df = pd.read_csv("masar_ai_dataset_v3_kaggle.csv")
    
    # 2. Le Pipeline IA (StandardScaler + K-Means) pour le jury
    theme_dummies = pd.get_dummies(df['primary_theme'], prefix='theme')
    numerical_features = df[['latitude', 'longitude', 'visit_duration_mins', 'economic_value_mad', 'accessibility_score']]
    X_raw = pd.concat([numerical_features, theme_dummies], axis=1)
    
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X_raw)
    
    kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
    df['route_cluster'] = kmeans.fit_predict(X_scaled)
    
    # 3. Filtrer par la thématique choisie sur le Front-end
    theme_df = df[df['primary_theme'] == theme].copy()
    if theme_df.empty:
        return []

    # 4. L'Heuristique de Routage (Plus Proche Voisin)
    places = theme_df.to_dict('records')
    
    # Pour le MVP, on garde les 5 meilleurs sites (les plus accessibles) pour une belle route
    places.sort(key=lambda x: x['accessibility_score'], reverse=True)
    places = places[:5] 
    
    route = []
    if not places: return route
    
    current_place = places.pop(0)
    route.append(current_place)
    
    while places:
        nearest_place = min(places, key=lambda p: calculate_distance(
            current_place['latitude'], current_place['longitude'],
            p['latitude'], p['longitude']
        ))
        route.append(nearest_place)
        places.remove(nearest_place)
        current_place = nearest_place

    return route