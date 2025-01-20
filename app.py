import streamlit as st
import pandas as pd

from bookkee.accounts import Account


def init_session_state():
    if 'data' not in st.session_state:
        st.session_state['accounts'] = {}

@st.dialog("New account")
def new_account():
    # TODO error if account name already exists
    account_name = st.text_input("Account name")
    filename = st.text_input("Save as ...", value = account_name+'.xlsx' )
    if not filename.endswith('.xlsx'):
         filename = filename + '.xlsx'
    if st.button("Submit"):
        st.session_state.accounts[account_name] = Account(file = filename)



def entry_point():
    if st.button('Create new account'):
        new_account()
    uploaded_file = st.file_uploader("Choose an existing accounting book")
    if uploaded_file is not None:
        st.session_state.accounts = Account.read_books(file = uploaded_file)
        # st.write(dataframe)
        bank_statement_file = st.file_uploader("Read a new bank statement")
        if bank_statement_file is not None:
            bank_statement = pd.read_excel(bank_statement_file)


if __name__ == "__main__":
    init_session_state()
    entry_point()