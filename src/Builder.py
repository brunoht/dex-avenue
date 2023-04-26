import pickle
import pandas as pd
from Recommender import Recommender
from Utils import data_path, models_path

files = {
    'train_sheet': '2023_03_03 - Ordens DNC.xlsx',
    'data_sheet': 'Dados DNC - Clientes, Ordens e Produtos_2.xlsx'
}

datasets = {
  'clientes': 'Reporting - Dados Perfil de Cli',
  'ordens': 'Reporting - Dados Ordens - Reco',
  'produtos': 'Reporting - Dados Produtos - Re'
}

# Get files
file_path1 = data_path(files['train_sheet'])
file_path2 = data_path(files['data_sheet'])

# Get data
df = pd.read_excel(file_path1)
df_produtos = pd.read_excel(file_path2, sheet_name=datasets['produtos'])
df_ordens = pd.read_excel(file_path2, sheet_name=datasets['ordens'])

# Get implicit ratings
def get_ratings(df: pd.DataFrame, df_ordens: pd.DataFrame) -> pd.DataFrame:
    NumProduto = pd.DataFrame(df.groupby('AccountID')['Symbol'].value_counts())
    NumProduto = NumProduto.rename({'Symbol': 'FreqSymbol'}, axis = 1)
    NumProduto = NumProduto.reset_index(level=['AccountID', 'Symbol'])

    totalFreq = NumProduto.groupby('AccountID')[['FreqSymbol']].sum()
    totalFreq = totalFreq.reset_index().rename({'FreqSymbol': 'TotalPeriodo'}, axis = 1)
    totalFreq

    NumProduto = NumProduto.merge(totalFreq, on = 'AccountID', how = 'left')
    NumProduto['FrequenciaSymbol'] = NumProduto['FreqSymbol']/NumProduto['TotalPeriodo']
    NumProduto = NumProduto.query('TotalPeriodo >= 3')
    FreqIndustria = NumProduto[['AccountID', 'Symbol', 'FrequenciaSymbol']]

    dfProduto = df_ordens.merge(FreqIndustria, on = ['AccountID', 'Symbol'], how = 'left')
    dfProduto = dfProduto.dropna()

    return dfProduto

# Get implicit ratings
df_ratings = get_ratings(df, df_ordens)

# Instiantiate recommender
recommender = Recommender(
    data=df_ratings,
    item_id='Symbol',
    user_id='AccountID',
    rating='FrequenciaSymbol'
)

# Train recommender
model, item_list, users_list = recommender.fit(min = 0.05)

# Save recommender
with open(models_path('main.pkl'), 'wb') as model_file:
    pickle.dump(recommender, model_file)


    