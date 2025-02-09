import pandas as pd
from contrato import Vendas 
import os

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
        return True, erros
        

    except Exception as e:
        return pd.DataFrame(), f"Erro inesperado: {str(e)}"
    

        

