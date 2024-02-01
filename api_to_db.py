import pandas as pd 
import sqlalchemy
import requests
from io import StringIO
from pandas import json_normalize
import json
from datetime import datetime, timedelta

def pull_from_covid_api():

    url =  "https://covid-19-statistics.p.rapidapi.com/reports"

    headers = {
	"X-RapidAPI-Key": "c448282c1fmsh57d073f04cc58a5p155dbfjsn2d33a8bc576c",
	"X-RapidAPI-Host": "covid-19-statistics.p.rapidapi.com" }

    # querystring = {"city_name":"Autauga","region_province":"Alabama","iso":"USA","region_name":"US","q":"US Alabama","date":"2020-04-16"}
    querystring = {"date":"2020-04-16"}

    dfs = []
    
    # start_date = datetime(2019, 1, 1)
    # end_date = datetime(2023, 12, 31)

    # current_date = start_date

    # while current_date <= end_date:
    response = requests.get(url,headers=headers,params=querystring)

    if response.status_code == 200:

        data = response.json()
        data = data['data']
        df = pd.DataFrame(data)           
        dfs.append(df)

    else:
        print("Failed to fetch data from the API")

    # current_date += timedelta(days=1)
    
    final_df = pd.concat(dfs, ignore_index=True)

    print(final_df.info())


def main():

    pull_from_covid_api()


main()
