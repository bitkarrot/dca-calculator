import requests
import pandas as pd
import time
import json

URL = "https://raw.githubusercontent.com/bitkarrot/satshkd-vercel/main/public/hkd_historical"

cache_data = {}
refresh_interval = 24 * 60 * 60  # 24 hours in seconds

def get_data():
    # Check if cached data exists and is less than 24 hours old
    if 'data' in cache_data and time.time() - cache_data['timestamp'] < refresh_interval:
        # Load data from cache
        df = pd.DataFrame(cache_data['data'])
        print(df.dtypes)
        
    else:
        # Fetch data from URL
        response = requests.get(URL)
        data = response.json()

        # Convert data to dataframe and save to cache
        df = pd.DataFrame(data)
        cache_data['data'] = df.to_dict('records')
        cache_data['timestamp'] = time.time()

    df['date'] = pd.to_datetime(df['date'])
    df['btcusd_rate'] = pd.to_numeric(df['btcusd_rate'])
    df['sathkd_rate'] = pd.to_numeric(df['sathkd_rate'])
    df['btchkd_rate'] = pd.to_numeric(df['btchkd_rate'])
    df['usdsat_rate'] = pd.to_numeric(df['usdsat_rate'])

    # Use the dataframe as needed
    return df


def get_data_from_file(datafile): 
    data = None
    with open(datafile, "+r") as f: 
        raw = f.read()
        data = json.loads(raw)
        df = pd.json_normalize(data)
        return df



if __name__ == "__main__": 
    # df = get_data()
    # print(df.head())
    # print(df.dtypes)
    datafile = "./btc_historical"
    dfile = get_data_from_file(datafile)
    print(dfile.head())
