import os
from mongoengine import connect

def connect_to_database():
    """Conects to a mongo instance given a valid connection string"""
    try:
        print("Establishing connection to database...")
        connection = connect(
            os.getenv('DATABASE'),
            host=os.getenv('HOST'),
            port=int(os.getenv('PORT')), 
            username=os.getenv('MONGO_USERNAME'), 
            password=os.getenv('PASSWORD'))
        print("Connected to database successfully")
        return connection
    except Exception as conn_err:
        print("Connection failed!")
        raise Exception(conn_err)
