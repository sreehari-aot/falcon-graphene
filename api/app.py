import falcon
from wsgiref.simple_server import make_server
from db import connect_to_database
from resource import CountryResource
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

app = falcon.App()

connect_to_database()

checkpoint = CountryResource()

app.add_route('/', checkpoint)


if __name__ == '__main__':
    with make_server('', 8000, app) as httpd:
        print('Serving on port 8000...')
        httpd.serve_forever()