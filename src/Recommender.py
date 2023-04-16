import pandas as pd
import networkx as nx
from collections import Counter

class Recommender:
  
    def __init__(self, data, item_id, user_id, rating):
        self.data = data.copy()
        self.item_id = item_id
        self.user_id = user_id
        self.rating = rating
    
    def fit(self, n_most_popular=10):
        G = nx.Graph()
        G.add_nodes_from(self.data['Symbol'].unique(), node_type='item')
        G.add_nodes_from(self.data['AccountID'].unique(), node_type='user')
        G.add_weighted_edges_from(self.data[['Symbol', 'AccountID', 'FrequenciaSymbol']].values)

        items_list_ = self.data['Symbol'].unique()
        
        users_list_ = self.data['AccountID'].unique()

        return G, items_list_, users_list_
        
    def recommend(self, G, target_item, max_recommendations=10):
        try:
            covisitation = self.recommend_neighbor_items(G, target_item, max_recommendations).drop(target_item, axis=0).index
            return covisitation          
        except KeyError as e:
            print(f'\033[1m{target_item}\033[0;0m is not included in the recommendation matrix.\n')
    
      
    def recommend_neighbor_items(self, G:nx.Graph, target_id, max_recommendations=10):
        
        # Validando tipo do nó
        node_type = nx.get_node_attributes(G, 'node_type')[target_id]
        if node_type != 'item':
            raise ValueError('Node is not of item type.')

        # Analisando consumo dos usuários vizinhos
        neighbor_consumed_items = []
        for user_id in G.neighbors(target_id):
            user_consumed_items = G.neighbors(user_id)
            neighbor_consumed_items +=list(user_consumed_items)

        # Contabilizando itens consumidos pelos vizinhos
        consumed_items_count = Counter(neighbor_consumed_items)

        # Criando dataframe
        df_neighbors = pd.DataFrame(zip(consumed_items_count.keys(), consumed_items_count.values()))
        df_neighbors.columns = ['item_id', 'score']
        df_neighbors = df_neighbors.sort_values(by='score', ascending=False).set_index('item_id')

        return df_neighbors.head(max_recommendations)
    
    def recommend_top_n_consumptions(self, ratings:pd.DataFrame, n:int) -> pd.DataFrame:
        recommendations = (
            ratings
            .groupby('Symbol')
            .count()['AccountID']
            .reset_index()
            .rename({'AccountID': 'score'}, axis=1)
            .sort_values(by='score', ascending=False)
        )
        return recommendations.head(n)
    
    def get_target(self, account_id):
        result = self.data.query('AccountID == @account_id')
        if result.size == 0: return None
        return result.sort_values('Date', ascending=False)['Symbol'].values[0]
    
    def get_data(self):
        return self.data