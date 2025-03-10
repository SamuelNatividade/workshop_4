import streamlit as st


    
class ExcelValidadorUI:

    def __init__(self):
        self.set_page_config()

    def set_page_config(self):
        st.set_page_config(
            page_title="Validador de Schema Excel"
        )

    def display_header(self):
        st.title("Validador de Schema Excel")


    def upload_file(self):
        return st.file_uploader("Carregue seu arquivo Excel aqui", type=["xlsx"])
    
    def display_results(self, result, error):
        if error:
                st.error(f"Erro na validacao: {error}")
        else:
            st.success("Validacao concluida com sucesso!")

    def display_save_button(self):
        return st.button("Salvar no banco de dados")
    
    def display_wrong_message(self, message):
        return st.error('Necessário corrigir a planilha')
    
    def display_success_message(self):
        return st.success('Dados salvos no banco de dados com sucesso!')
    


