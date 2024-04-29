# %% [markdown]
# <h2 style="text-align: center;">Imports</h2>

# %%
import pandas as pd 
import numpy as np
import xml.etree.ElementTree as ET
import requests
import json

# %% [markdown]
# <h2 style="text-align: center;">Local and Constant Variables</h2>

# %%
pd.options.display.max_columns = None # show all columns in display

# %%
# read api keys file and assign variables
df = pd.read_csv("api_keys.csv")
zwsid = df.loc[df['API'] == 'rapid']['KEY'].iloc[0]

# %% [markdown]
# <h2 style="text-align: center;">Functions</h2>

# %%
def zillow_get_search_result	(zwsid,
                            	street,
                             	city,
								state,
                             	zip_code):
    url = "https://zillow-com4.p.rapidapi.com/properties/search-address"

    querystring = {"address":"104 Meir Ln College Station, TX 77845"}

    headers = {
        "X-RapidAPI-Key": str(zwsid),
        "X-RapidAPI-Host": "zillow-com4.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    return response

def zillow_parse_search_results(response):
    data = response.json()

    if response.status_code == 200:
        print("Address:", ", ".join([loc['fullValue'] for loc in data['data']['formattedChip']['location']]))
        print("Home Type:", data['data']['homeType'])
        print("Home Type:", data['data']['resoFacts']['yearBuilt'])
        print("Sqft:", data['data']['formattedChip']['quickFacts'][2]['value']['fullValue'])
        print("Lot Area:", data['data']['lotAreaValue'])
        print("Beds:", data['data']['formattedChip']['quickFacts'][0]['value']['fullValue'])
        print("Baths:", data['data']['formattedChip']['quickFacts'][1]['value']['fullValue'])
        print("Zestimate Value:", data['data']['formattedChip']['additionalFacts'][0]['value']['fullValue'])
        print("Longitude:", data['data']['longitude'])
        print("Latitude:", data['data']['latitude'])
        print("Price:", data['data']['price'])
        print("Zestimate:", data['data']['zestimate'])
    else:
        print("Error:", response.status_code)
    return


# %% [markdown]
# <h2 style="text-align: center;">Data</h2>

# %%
# address parameters
street = "104 Meir Ln"
city = "College Station"
state = "TX"
zip_code = "77845"

# %%
result = zillow_get_search_result(zwsid, street, city, state, zip_code) 
zillow_parse_search_results(result)


