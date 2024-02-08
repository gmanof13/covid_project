from sqlalchemy import create_engine
import psycopg2 
import json
import pandas as pd
import os

engine = create_engine('postgresql+psycopg2://postgres:admin@localhost:5432/covid') 

def json_dir_to_db(table_name: str, json_dir_path: str):
    # Get a list of all JSON files in the directory
    json_files = [file for file in os.listdir(json_dir_path) if file.endswith('.json')]

    # Iterate over each JSON file
    for json_file in json_files:
        # read json into pandas df
        with open(os.path.join(json_dir_path, json_file), "r") as file:
            data = json.load(file)
        
        df = pd.json_normalize(data, record_path='data', max_level=1)
        df = df.drop('region.cities', axis=1)
        

    # write combined DataFrame into the database
    # engine = create_engine('postgresql+psycopg2://postgres:admin@localhost:5432/covid') 
        df.to_sql(table_name, engine, if_exists='append', index=False)

json_dir_to_db(table_name='covid_tbl', json_dir_path="D:/python_projects/covid_project/json_dir")