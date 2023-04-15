import pandas as pd

print('Conheça o time:')

print()

data = {
    'name': ['Bruno Henrique', 'Marcos'],
    'email': ['bruno@lohl.com.br', 'marcos@gmail.com']
}

df = pd.DataFrame(data)

print(df)

print()

print('Teste finalizado com sucesso!')
