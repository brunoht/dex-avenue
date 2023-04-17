import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../src')

import pickle
import uvicorn
import pandas as pd
from fastapi import FastAPI
from Utils import response, models_path, env

# Application

app = FastAPI()

# GET Index
@app.get("/")
def index():
    return response({
        'application': 'dex-avenue-api',
        'version': '1.0.0'
    })

# Load Model
with open(models_path('main.pkl'), 'rb') as file:
    
    recommender = pickle.load(file)
    model, item_list, users_list = recommender.fit()

    # GET Accounts
    @app.get("/accounts")
    def accounts(limit = 5):
        users = pd.Series(users_list.tolist())
        accounts = users.head(int(limit)).tolist()
        
        return response({
            'limit': limit,
            'accounts': accounts
        })

    # GET Recommend
    @app.get("/recommend/{account_id}")
    def recommend(account_id):
        target = recommender.get_target(account_id)
        if target is None: return response(success=False)
        
        recommendation = recommender.recommend(model, target)
        
        if recommendation is not None:    
            type = 'covisitation'
            recommendation_list = recommendation.tolist()
        else: 
            type = 'top_n'
            recommendation_list = recommender.recommend_top_n_consumptions(recommender.get_data(), n=10).Symbol.tolist()
        
        return response({
            'account_id': account_id,
            'target': target,
            'type': type,
            'recommendation': recommendation_list
        })


if __name__ == '__main__':
    uvicorn.run(
        app, 
        host = env('HOST'), 
        port = env('PORT', 'int')
    )