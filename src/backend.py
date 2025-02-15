import pandas as pd
from contrato import Vendas 
import os
from dotenv import load_dotenv


 # Lê as variáveis de ambiente
load_dotenv('tests/.env')

POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
POSTGRES_HOST = os.getenv('POSTGRES_HOST')
POSTGRES_PORT = os.getenv('POSTGRES_PORT')
POSTGRES_DB = os.getenv('POSTGRES_DB')

# Cria a URL de conexão com o banco de dados
DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
print(DATABASE_URL)

def process_excel(uploaded_file):
    try:
        df = pd.read_excel(uploaded_file)
        erros = []
        # verificar se existe colunas extras no dataframe
        extra_cols = set(df.columns) - set(Vendas.model_fields.keys())
        if extra_cols:
            return False, f"Colunas extras detectadas no excel: {' '', '.join(extra_cols)}"
        

        # Validar cada linha com o schema escholido
        for index, row in df.iterrows():
            try:
                _ = Vendas(**row)
            except Exception as e:
                erros.append(f"Linha {index + 2}: {e}")

        # Retona tanto or esultado resultado da valida;ao, os erros e o dataframe
        return df, True, None
        

    except ValueError as ve:
        return df, False, str(ve)
    except Exception as e:
        return df, False, f"Erro inesperado: {str(e)}"
    

def excel_to_sql(df):
    # Escreve o DataFrame no banco de dados
    df.to_sql('vendas', con=DATABASE_URL, if_exists='replace', index = False)
    
        

