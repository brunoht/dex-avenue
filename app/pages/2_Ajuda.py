import streamlit as st

st.set_page_config(
    page_title="Ajuda | DEX Avenue Playground"
)

st.title('Ajuda')

st.write('Instruções de implementação do modelo Pickle (pkl)')

st.markdown('''
GITHUB: [https://github.com/brunoht/dex-avenue](https://github.com/brunoht/dex-avenue)
### Carregar o modelo

Antes de executar qualquer operação do recomendadador é 
necessário carregar uma instância do modelo:

```python
with open(models_path('main.pkl'), 'rb') as file:
    recommender = pickle.load(file)
    model, item_list, users_list = recommender.fit()
```

### Obter lista de usuários

```python
users = users_list.tolist()
```

#### Converter lista em Dataset

```python
users = pd.Series(users_list.tolist())
```

#### Controlar o número de resultados a serem exibidos

```python
users = pd.Series(users_list.tolist())
users = users.head(int(limit)).tolist()
```

## Recomendação

```python
target = recommender.get_target(account_id)
recommendation = recommender.recommend(model, target)

if recommendation is not None:    
    type = 'covisitation'
    recommendation_list = recommendation.tolist()
else: 
    type = 'top_n'
    recommendation_list = recommender.recommend_top_n_consumptions(recommender.get_data(), n=10).Symbol.tolist()
```
''')

