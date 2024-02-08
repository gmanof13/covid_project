import pandas as pd 
import sqlalchemy
import requests
from io import StringIO
from pandas import json_normalize
import json
from datetime import datetime, timedelta
import os
import shutil
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists,create_database
import contextlib
import sqlite3
import logging
import time 

# logging
logging.basicConfig(filename='api_to_json.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

def create_json_dir(testing: bool = True):
    """Creates JSON directory, if it doesn't exist."""

    if testing == True:

        if os.path.exists('json_dir'):
            shutil.rmtree('json_dir') 
            os.mkdir('json_dir')
        else:
            os.mkdir('json_dir')
    else:

        None


def api_to_json_dir():
    """Pulls JSON into local directory"""
    
    url =  "https://covid-19-statistics.p.rapidapi.com/reports"
    
    headers = {
        "X-RapidAPI-Key": "c448282c1fmsh57d073f04cc58a5p155dbfjsn2d33a8bc576c",
        "X-RapidAPI-Host": "covid-19-statistics.p.rapidapi.com" 
    }

    start_date = datetime(2021, 1, 1)
    end_date = datetime(2022, 12, 31)

    current_date = start_date
    while current_date <= end_date:
        querystring = {"date": current_date.strftime("%Y-%m-%d")}
        try:
            response = requests.get(url, headers=headers, params=querystring)
            response.raise_for_status()  # Raise an exception for bad response status
            data = response.json()
            with open(f"json_dir/covid_{current_date.strftime('%Y-%m-%d')}.json", "w") as file:
                json.dump(data, file)
        except requests.exceptions.RequestException as e:
            error_msg = f"Failed to fetch data for date {current_date}: {e}"
            logging.error(error_msg)
            time.sleep(5) # API can't handle async lol
            # You can choose to handle the error as needed
            pass
        
        current_date += timedelta(days=1)


def create_db(testing: bool):

    if testing == True:
        conn = sqlite3.connect('covid.db')
    else:
        None


def json_dir_to_db(db_name: str):

    # read json into pandas df
    with open("D:/python_projects/covid_project/json_dir/covid.json","r") as file:
        data = json.load(file)
    df = pd.json_normalize(data,record_path='data',max_level=1)
    df = df.drop('region.cities', axis=1)
    
    # write pandas df into db
    conn = sqlite3.connect('covid.db')
    df.to_sql(f'{db_name}', conn, if_exists='replace')


def main():

    create_json_dir(testing=False)
    api_to_json_dir()
    # create_db(testing=False)
    # json_dir_to_db(db_name='covid_tbl')




if __name__ == "__main__":
    main()