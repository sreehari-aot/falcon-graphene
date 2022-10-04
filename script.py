from typing import List, AnyStr
import requests

from schema import CountrySchema
from model import Country
from mongoengine import connect

API_URL = "https://restcountries.com/v3.1/all"
CONNECTION_STRING= "mongodb://mongoadmin:secret@192.168.82.1:27017/"

def fetch_data(url: AnyStr) -> List:
    """Fetch the data from the given API and validate."""
    print("Fetching data...")
    response = requests.get(url)
    if response.status_code == 200:
        print("data fethed successfully!")
    schema = CountrySchema()
    data = schema.load(response.json(), many=True)
    return data

def connect_to_database(connection_string: AnyStr):
    """Conects to a mongo instance given a valid connection string"""
    try:
        print("Establishing connection to database...")
        connection = connect(host=connection_string)
        print("Connected to database successfully")
        return connection
    except Exception as conn_err:
        print("Connection failed!")
        raise Exception(conn_err)

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
    connect_to_database(connection_string=CONNECTION_STRING)
    save_to_database(data)