import pandas as pd

# Cargar archivos
ratings = pd.read_csv('u.data', sep='\t', 
                      names=['user_id','item_id','rating','timestamp'])

users = pd.read_csv('u.user', sep='|', 
                    names=['user_id','age','gender','occupation','zip'])

movies = pd.read_csv('u.item', sep='|', encoding='latin-1',
                     names=['item_id','title','release_date','video_release',
                            'imdb_url'] + [f'genre_{i}' for i in range(19)])

# Unir ratings con usuarios
df = ratings.merge(users, on='user_id')

# Unir con películas (solo agregamos el título para no hacer el archivo gigante)
df = df.merge(movies[['item_id','title']], on='item_id')

# Guardar como CSV
df.to_csv('movielens_completo.csv', index=False)

print("Archivo guardado como movielens_completo.csv")
print(df.head())
