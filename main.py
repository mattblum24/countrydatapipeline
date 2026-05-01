import requests
import numpy as np
import pandas as pd

def get_data():
    url = f"https://restcountries.com/v3.1/all?fields=name,capital,currencies"
    response = requests.get(url)

    print(response.status_code)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None


country_data = get_data()
if country_data is not None:
    print("Successfully retrieved data")
else:
    print('Failed to retrieve data')

# df = pd.read_json(country_data)

