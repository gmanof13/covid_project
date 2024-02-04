import pandas as pd 
import sqlalchemy
import requests
from io import StringIO
from pandas import json_normalize
import json
from datetime import datetime, timedelta
import os
import shutil

def create_json_dir(testing: bool = True):

    if testing == True:

        if os.path.exists('json_dir'):
            shutil.rmtree('json_dir') 
            os.mkdir('json_dir')
        else:
            os.mkdir('json_dir')
    else:

        pass 

# todo: need to loop through querystring data field to append multiple JSONs by date. Then, at some point, check for missing dates???
def api_to_json_dir():

    url =  "https://covid-19-statistics.p.rapidapi.com/reports"
    
    headers = {
	"X-RapidAPI-Key": "c448282c1fmsh57d073f04cc58a5p155dbfjsn2d33a8bc576c",
	"X-RapidAPI-Host": "covid-19-statistics.p.rapidapi.com" }

    querystring = {"date":"2020-04-16"}

    response = requests.get(url,headers=headers,params=querystring)

    data = response.json()

    with open("json_dir/covid.json","w") as file:
        json.dump(data,file)
    
def create_db():
    pass 

def json_dir_to_db():
    pass

def main():

    create_json_dir(testing=False)
    api_to_json_dir()

if __name__ == "__main__":
    main()