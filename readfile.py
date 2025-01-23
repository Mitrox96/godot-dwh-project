import pyarrow.parquet as pq

# Lire le fichier Parquet
table = pq.read_table("releases.parquet")

# Afficher les données
print(table)

# Convertir en DataFrame (si nécessaire)
df = table.to_pandas()
print(df.head())
# Charger les stargazers
stargazers_table = pq.read_table("stargazers.parquet")

# Afficher les premières lignes des données
print(stargazers_table.to_pandas().head())
