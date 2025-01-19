import streamlit as st
import pandas as pd

from bookkee.accounts import sheet_names, empty_data, columns
from bookkee.accounts import read_books


def init_session_state():
    if 'data' not in st.session_state:
        st.session_state['data'] = empty_data

@st.dialog("New account")
def new_account(data):
    account_name = st.text_input("Account name")
    filename = st.text_input("Save as ...", value = account_name+'.xlsx' )
    if not filename.endswith('.xlsx'):
         filename = filename + '.xlsx'
    if st.button("Submit"):
        for sheet in sheet_names:
            data[sheet][account_name] = columns[sheet]
            data['filename'][account_name] = filename



def entry_point():
    if st.button('Create new account'):
        new_account(st.session_state['data'])
    st.write('DEBUG ', st.session_state['data']['book'])
    uploaded_file = st.file_uploader("Choose an existing accounting book")
    if uploaded_file is not None:
        full_books = read_books(uploaded_file)
        # st.write(dataframe)
        bank_statement_file = st.file_uploader("Read a new bank statement")
        if bank_statement_file is not None:
            bank_statement = pd.read_excel(bank_statement_file)


if __name__ == "__main__":
    init_session_state()
    entry_point()