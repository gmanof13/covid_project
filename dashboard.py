import sqlite3
import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt

def return_db_df():

    table = 'covid_tbl'
    conn = sqlite3.connect('covid.db')
    df = pd.read_sql(f'select * from {table}',conn)
    df = df[['confirmed']]
    return df
    conn.close()

def generate_hist_chart(kind: str,df: pd.DataFrame):

    if kind == 'hist':
        plt.hist(df,bins=5)
        st.pyplot()
    else: 
        None

def main():

    pandas_df = return_db_df()
    generate_hist_chart(kind='hist',df=pandas_df)
    
    
if __name__ == '__main__':
    main()