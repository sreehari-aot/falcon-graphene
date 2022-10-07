# Get started
1. Stand up a mongo instance

      Docker:-
      
         docker run -d -p 27017:27017 --name mongoDB -e MONGO_INITDB_ROOT_USERNAME=mongoadmin -e MONGO_INITDB_ROOT_PASSWORD=secret mongo:latest
         
2. Clone this repository

      `https://github.com/sreehari-aot/falcon-graphene.git`
      
3. Create virtual environment and activate
    
      https://docs.python.org/3/library/venv.html
      
4. Install dependencies
      
      `pip install -r requirements.txt`
      
5. Rename `sample.env` to `.env`

6. run `python script.py`
      
      data should be saved to the database if all the steps are followed as mentioned
      
7. Starting the application server
  
    - check into `/api` directory
    - run `python app.py`
    
    application server should be up and running by now
    
8. Query data with Grapghql

    - countriesQuery - return a list of countries
    
        ```
        query {
            countries {
                name
                currencies
                capital
                language
                latlng
                maps
                population
                continents
                flags
                postalCode
            }
        }

        ```
     - countryQuery - take country id as an argument and return details of single country raise error if id is invalid
        
        ```
        query {
            country (id: "{country id}") {
                name
                ...
            }
        }

        ```
        
      - countriesNearby - take location cocordinates and return list of nearest countries
          
          ```
          query {
              nearby (coordinates: [{lat}, {lng}]) {
                  name
                  ...
              }
          }
          ```
       
       - countriesByLanguage - take a language string and return a list of countries speaking that language
       
          ```
          query {
              lang (language: "English") {
                  name
                  ...
              }
          }
          ```
          
          
