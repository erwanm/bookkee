import streamlit as st
import pandas as pd

from bookkee.accounts import Account


# TODO must have a general config with:
# - default_account
#

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
        new_accounts = Account.read_books(filename_or_object = uploaded_file)
        for new_account_name in new_accounts.keys():
            if new_account_name in st.session_state.accounts.keys():
                raise Exception(f'Account {new_account_name} already exists in current books.')
        st.session_state.accounts = st.session_state.accounts | new_accounts
        # st.write(dataframe)
    if len(st.session_state.accounts) > 0:
        bank_statement_file = st.file_uploader("Read a new bank statement")
        if bank_statement_file is not None:
            bank_statement = pd.read_excel(bank_statement_file)
            if st.session_state.conf['default_account'] is not None:
                account = st.session_state.conf['default_account']
            if account is None and len(st.session_state.accounts) == 1:
                account = list(st.session_state.accounts.values())[0]
            else:
                st.selectbox('Select account:', st.session_state.accounts.values())


if __name__ == "__main__":
    init_session_state()
    entry_point()
