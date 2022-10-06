import os
import requests

from dotenv import find_dotenv, load_dotenv
from typing import List, AnyStr
from schema import CountrySchema
from api.model import Country
from api.db import connect_to_database

load_dotenv(find_dotenv())

#Datasource
API_URL = os.getenv("API_URL")

def fetch_data(url: AnyStr) -> List:
    """Fetch the data from the given API and validate."""
    print("Fetching data...")
    response = requests.get(url)
    if response.status_code == 200:
        print("data fethed successfully!")
    schema = CountrySchema()
    data = schema.load(response.json(), many=True)
    return data


def save_to_database(data: List) -> None:
    """Persist the given data in the database."""
    try:
        print("Saving data...")
        country_instances = [Country(**object) for object in data]
        Country.objects.insert(country_instances, load_bulk=False)
        print("Data saved to database!")
    except Exception as err:
        raise Exception(err)

if __name__ == "__main__":
    data = fetch_data(API_URL)
    connect_to_database()
    save_to_database(data)
