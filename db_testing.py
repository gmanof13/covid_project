import sqlite3
import pandas as pd

def test_db_pandas(table: str):
    conn = sqlite3.connect('covid.db')
    df = pd.read_sql(f'select * from {table}',conn)
    return df
    conn.close()


def show_all_tables():
    
    con = sqlite3.connect('covid.db')
    cur = con.cursor()
    cur.execute('''
                
        SELECT tbl_name
        FROM sqlite_master
        WHERE type = 'table';
                
    ''')

    return cur.fetchall()

df_test = test_db_pandas(table='covid_tbl')

show_tables_df = show_all_tables()

print(show_tables_df)

