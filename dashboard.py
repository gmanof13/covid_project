import sqlite3
import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt

def return_covid_df():

    table = 'covid_tbl'
    conn = sqlite3.connect('covid.db')
    df = pd.read_sql(f'select * from {table}',conn)
    df['date']= pd.to_datetime(df['date'])
    return df
    conn.close()

def return_time_series_graph(df: pd.DataFrame) -> None: 
    st.line_chart(df[['date','confirmed']],x='date',y='confirmed')


def main():

    time_series_df = return_covid_df()
    return_time_series_graph(time_series_df)
    # return_time_series_graph(time_series_df)
    

    
    
if __name__ == '__main__':
    main()