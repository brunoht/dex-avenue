import sys
import pickle
import uvicorn
import pandas as pd
from fastapi import FastAPI

# Inicia API
app = FastAPI()

# Carrega modelo
sys.path.append('src')
with open('models/recommender.pkl', 'rb') as file:
    recommender = pickle.load(file)

# Cria página inicial
@app.get('/')
def home():
    return 'Welcome to the Avenue Recommender app!'

# Lista jogos
@app.get('/list_recommend')
def list_recommend():
    model, item_list = recommender.fit()
    return item_list.tolist()

# Procura jogos por substring
@app.get('/search_recommender')
def search_recommender(pattern):
    pattern = pattern.lower()
    model, item_list = recommender.fit()
    lista = pd.Series(item_list.tolist())
    lista_matched = lista[lista.str.lower().str.contains(pattern)]
    return lista_matched

# Recomenda jogo
@app.get('/recommend')
def recommend(target: str, max_recommendations: int = 10):
    model, item_list = recommender.fit()
    return recommender.recommend(model, target).tolist()

# Executa API
if __name__ == '__main__':
    uvicorn.run(app)
