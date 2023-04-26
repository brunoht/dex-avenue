import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../src')

import pickle
import pandas as pd
import streamlit as st
from Utils import *

## -- Page Settings -- ##

title = "DEX Avenue Playground"

st.set_page_config(page_title=title)

with open (models_path('main.pkl'), 'rb') as file:
  
  # load data
  
  recommender = pickle.load(file)
  
  model, item_list, users_list = recommender.fit()
  
  users = pd.Series(users_list.tolist())
  
  ## -- Page Content -- ##
  
  st.title(title)
  
  ## -- Parameters -- ##
  
  users_limit = st.number_input('Número de clientes', min_value=5, max_value=100, value=5)

  n_recommendations = st.number_input('Número de recomendações', min_value=5, max_value=20, value=10)
  
  account_id = st.selectbox('Selecione um cliente [Account ID]', users.head(users_limit).tolist())

  target = recommender.get_target(account_id)
  
  result = recommender.recommend(model, target, max_recommendations=n_recommendations, drop = False)

  
  ## -- Model Result -- ##
  
  if result is not None:
    
    st.write(f'Quem comprou **{target}**, também comprou:')
    
    st.write(result.tolist())
    
  else: 
    
    st.write(f'Não há recomendações para **{target}**. Veja os mais comprados:')
    
    st.write(recommender.recommend_top_n_consumptions(recommender.get_data(), n=10).Symbol.tolist())

