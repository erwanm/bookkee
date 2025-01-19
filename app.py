import streamlit as st
import pandas as pd


def read_books():


def entry_point():
    uploaded_file = st.file_uploader("Choose an existing accounting book")_
    if uploaded_file is not None:
        full_books = read_books(uploaded_file)
        # st.write(dataframe)
        bank_statement_file = st.file_uploader("Read a new bank statement")
        if bank_statement_file is not None:
            bank_statement = pd.read_excel(bank_statement_file)


if __name__ == "__main__":
    entry_point()