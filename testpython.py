import requests
import pyarrow.parquet as pq
import pyarrow as pa

BASE_URL = "https://api.github.com/repos/godotengine/godot"
HEADERS = {"Authorization": ""} 

def fetch_data(endpoint):
    url = f"{BASE_URL}{endpoint}"
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Erreur : {response.status_code} - {response.text}")
        return []

releases = fetch_data("/releases")
if releases:
    releases_table = pa.Table.from_pylist(releases)
    pq.write_table(releases_table, "releases.parquet")
    print("Données des releases sauvegardées dans releases.parquet")

stargazers = fetch_data("/stargazers")
if stargazers:
    stargazers_table = pa.Table.from_pylist(stargazers)
    pq.write_table(stargazers_table, "stargazers.parquet")
    print("Données des stargazers sauvegardées dans stargazers.parquet")

traffic_clones = fetch_data("/traffic/commits")
if traffic_clones:
    traffic_table = pa.Table.from_pylist(traffic_clones["clones"])
    pq.write_table(traffic_table, "traffic_clones.parquet")
    print("Données des clones sauvegardées dans traffic_clones.parquet")

