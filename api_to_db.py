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

# todo: need to loop through querystring data field to append multiple JSONs by date. Then, at some point, check for missing dates???
def api_to_json_dir():

    """Pulls JSON into local directory"""

    url =  "https://covid-19-statistics.p.rapidapi.com/reports"
    
    headers = {
	"X-RapidAPI-Key": "c448282c1fmsh57d073f04cc58a5p155dbfjsn2d33a8bc576c",
	"X-RapidAPI-Host": "covid-19-statistics.p.rapidapi.com" }

    querystring = {"date":"2020-04-16"}

    response = requests.get(url,headers=headers,params=querystring)

    data = response.json()

    with open("json_dir/covid.json","w") as file:
        json.dump(data,file)


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

    # create_json_dir(testing=False)
    # api_to_json_dir()
    # create_db(testing=True)
    json_dir_to_db(db_name='covid_tbl')



if __name__ == "__main__":
    main()