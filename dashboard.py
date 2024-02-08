import sqlite3
import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

engine = create_engine('postgresql+psycopg2://postgres:admin@localhost:5432/covid')



def main():
    
    df = pd.read_sql_query('select * from "covid_tbl"',con=engine)


    print(df.info())

    
    
if __name__ == '__main__':
    main()