# Udacity FSND Capstone

The casting agency project. it's the capstone project of Udacity to demonstrate the fullstack skills that students get during the nano-degree.
The back-end service in this project, is based on Role-Based Authentication and Authorization, so for the user to access the services, he/she need to have an account with privligies.

to build this project, I have used, 
- Python and Flask to build the backend-server
- Auth0 as third-party for Authentication and Authorization process.
- Heroku to deploy the application on using github as pipeline. 

## Getting Started

### Installing Dependencies

To start the project locally, you need to have the following tools:
- Python3 and pip or pip3

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by navigating to the root of the directory and run:

```bash
pip install -r requirements.txt
```

install all packages in the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 


## Running the server locally in development environment

in the `root` of the project directory.

To run the server:

```bash
pip install -r requirements.txt
source setup.sh
python app.py
```

the `source setup.sh` contain all environment variables.

NOTE: you need to make changes to the `setup.sh` file, if you would like to run it locally. 

#### Testing

for tests, run:
```
dropdb capstonefsnd_test
createdb capstonefsnd_test
source setup.sh
python test_app.py
```

## API Reference

### Introduction

The API builded to make users with specific roles to be eable to perform CRUD operations on the Agency database. It have been builded using Flask.
This API was builded for the requirments of graduating of the FSND nanodegree scolarship of Udactiy.
All the responses of the API is in JSON format.

### Getting Started

#### Base URL

This project is available on:
```
https://sohaibcapstone.herokuapp.com/
```

### Error

The API have clear and defined errors that will make the debug process easier for developers.

#### Error Types:

- 404 - Not Found
- 400 - Bad Request
- 422 - Unprocesaable
- 401 - Unauthorized

#### Error Response Example:

```
{
    "success": False,
    "error": 404,
    "message": "Resource Not Found"
}
```

### Endpoints Library

This section will contain all the endpoints with their response examples to make everything clear for the users of our API

#### GET /actors

- Return: return list of all the available actors.

- Sample Request: ```curl https://sohaibcapstone.herokuapp.com/actors```

- Arguments: None

- Sample Response:
    ```
    {
          "success": True,
          "actors": [
            {
              "id": 1,
              "name": "Sohaib Bakri",
              "gender": "male",
              "age": 20
            }, 
            {
              "id": 2,
              "name": "Meshaal Al-bishi",
              "gender": "male",
              "age": 20
            }
          ]
    }
    ```
#### GET /movies

- Return: return list of all the available movies.

- Sample Request: ```curl https://sohaibcapstone.herokuapp.com/movies```

- Arguments: None

- Sample Response:
    ```
    {
          "success": True,
          "movies": [
            {
              "id": 1,
              "title": "Bad Blood",
              "release": "09 April, 2020"
            }, 
            {
              "id": 2,
              "title": "GOF",
              "release": "22 Sep, 2021"
            }
          ]
    }
    ```

#### DELETE /actors/id

- Return: 
    - the deleted actor ID and result of success state.

- Sample Request: ```curl -X "DELETE" https://sohaibcapstone.herokuapp.com/actors/2```

- Arguments: 
    - it take the id of the actor in the URL after the ```actors/```

- Sample Response:
    ```
    {
        "success": True,
        "actor_id": 2
    }
    ```

#### DELETE /movies/id

- Return: 
    - the deleted movie ID and result of success state.

- Sample Request: ```curl -X "DELETE" https://sohaibcapstone.herokuapp.com/movies/5```

- Arguments: 
    - it take the id of the movie in the URL after the ```movies/```

- Sample Response:
    ```
    {
        "success": True,
        "movie_id": 2
    }
    ```

#### POST /actors

- Return: 
    - the request success state.
    - the created actor object.

- Sample Request: 
    ```curl -d '{"name": "Sohaib Bakri", "age": 21, "gender": "male"}' -H "Content-Type: application/json" -H "Authorization: Bearer <TOKEN>" -X "POST" https://sohaibcapstone.herokuapp.com/actors```

- Arguments: 
    - None

- Required Headers:
    - authorized and valid JWT token.
    - Content-Type: application/json

- Sample Response:
    ```
    {
        "success": True,
        "actor": {
            "id": 3,
            "name": "Sohaib Bakri",
            "gender": "male",
            "age": 21
        }
    }
    ```

#### POST /movies

- Return: 
    - the request success state.
    - the created movie object.

- Sample Request: 
    ```curl -d '{"title": "Bad Bunny"}' -H "Content-Type: application/json" -H "Authorization: Bearer <TOKEN>" -X "POST" https://sohaibcapstone.herokuapp.com/movies```

- Arguments: 
    - None

- Required Headers:
    - authorized and valid JWT token.
    - Content-Type: application/json

- Sample Response:
    ```
    {
        "success": True,
        "movie": {
            "id": 17,
            "title": "Bad Bunny",
            "release": "8 Sep, 2021"
        }
    }
    ```

#### PATCH /actors

- Return:
    - the request success state.
    - the modified actor object.

- Sample Request: 
    ```curl -d '{"name": "sohaib bkr", "age": 17, "gender": "male"}' -H "Content-Type: application/json" -H "Authorization: Bearer <TOKEN>" -X "PATCH" https://sohaibcapstone.herokuapp.com/actors/15```

- Arguments: 
    - the ID of the actor that need to modified.

- Required Headers:
    - authorized and valid JWT token.
    - Content-Type: application/json

- Sample Response:
    ```
    {
        "success": True,
        "actor": {
            "id": 3,
            "name": "sohaib bkr",
            "gender": "male",
            "age": 17
        }
    }
    ```

#### PATCH /movies

- Return:
    - the request success state.
    - the modified movie object.

- Sample Request: 
    ```curl -d '{"title": "bad punny"}' -H "Content-Type: application/json" -H "Authorization: Bearer <TOKEN>" -X "PATCH" https://sohaibcapstone.herokuapp.com/movies/87```

- Arguments: 
    - the ID of the movie that need to modified.

- Required Headers:
    - authorized and valid JWT token.
    - Content-Type: application/json

- Sample Response:
    ```
    {
        "success": True,
        "movie": {
            "id": 17,
            "title": "bad punny",
            "release": "8 Sep, 2021"
        },
        "movie_id": 17
    }
    ```

## Authentication and Priviligies

Authentication is handled via [Auth0](https://auth0.com).

For testing, use the Tokens available in the setup.bash file.

API endpoints use these roles and priviligies:

- Casting Assistant:
    * 'get:movies' (get all the movies that available)
    * 'get:actors' (get all the actors that available)

- Casting Director:
    * Same as the Casting Assistant priviligies, and
    * 'delete:actor' (delete actor agency casting database).
    * 'patch:actor' (update actor data in the casting agency database).
    * 'patch:movie' (update actor data in the casting agency database).
    * 'post:actors' (create new actors record in the casting agency database).

- Executive Producer:
    * Same as the Casting Director priviligies, and
    * 'delete:movie' (remove movie from the casting agency database).
    * 'post:movies' (create new movies in the casting agency database).


## Authors

I'am Sohain Bakri, I Authored the following code and files:
- app.py 
- models.py
- test_app.py
- config.py
- README.md
