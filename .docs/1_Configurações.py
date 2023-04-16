import streamlit as st

st.set_page_config(
    page_title="Configurações | DEX Avenue Playground"
)

st.title('Configurações')

st.markdown('''
> Esta funcionalidade não está disponível nesta versão!
''')

st.markdown('''
### Train dataset upload
''')

train_dataset_file = st.file_uploader('Envie o arquivo que contém o dataset de treinamento')

if train_dataset_file:
    st.write(train_dataset_file)
    
st.markdown('''
            ---
### Dataset upload
''')

dataset_file = st.file_uploader('Envie o arquivo que contém o dataset atualizado', )

if dataset_file:
    st.write(dataset_file)