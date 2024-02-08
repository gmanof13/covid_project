import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

engine = create_engine('postgresql+psycopg2://postgres:admin@localhost:5432/covid')


def create_line_graph():

    df = pd.read_sql(con=engine,sql="select * from us_deaths_time_series_tbl")
    df = df[['date','sum_deaths']]
    df['date'] = pd.to_datetime(df['date'])
    st.line_chart(df,x='date',y='sum_deaths')
    st.title("US Covid Deaths Over Time")
    
if __name__ == '__main__':
    create_line_graph()