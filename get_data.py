# raw data, daily history data source
# https://raw.githubusercontent.com/bitkarrot/satshkd-vercel/main/public/hkd_historical

# Data format
# [{"btcusd_rate":0.0858,"date":"2010-07-18","usdsat_rate":1165501166,
# "sathkd_rate":"150387247","btchkd_rate":"0.66"},.....]

import requests
import pandas as pd

source_url = "https://raw.githubusercontent.com/bitkarrot/satshkd-vercel/main/public/hkd_historical"

response = requests.get(source_url)
data = response.json()

df = pd.DataFrame(data)
print(df)
