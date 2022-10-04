import json
import string
import requests

from schema import CountrySchema
from mongoengine import connect

API_URL = "https://restcountries.com/v3.1/all"
CONNECTION_STRING= "mongodb://mongoadmin:secret@192.168.82.1:27017/"

# convert this as a fetcher function
response = requests.get(API_URL)
schema = CountrySchema()
data = schema.load(response.json(), many=True)

# can be removed just to see the structure
with open("data.json","w") as outfile:
    outfile.write(json.dumps(data))


def connect_to_database(connection_string: string):
    """Coonects to a mongo instance given a valid connection string"""
    try:
        connection = connect(host=connection_string)
        print("Connected to database successfully")
        return connection
    except Exception:
        print("Connection failed!")
        raise(Exception)

if __name__ == "__main__":
    connect_to_database(connection_string=CONNECTION_STRING)