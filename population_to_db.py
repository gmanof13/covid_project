import pandas as pd
import psycopg2
from sqlalchemy import create_engine


engine = create_engine('postgresql+psycopg2://postgres:admin@localhost:5432/covid')
population_df = pd.read_excel('D:/python_projects/covid_project/population_data/uszips.xlsx')

def df_to_db(table_name: str, df: pd.DataFrame):

    df.to_sql(table_name, engine, if_exists='append', index=False)

df_to_db(table_name='population_tbl',df=population_df)
