# Minimal REST API Microservice

A minimal REST API microservice in python built with Flask.

This is a simple microservice boilerplate written in python using Flask. 
It was built to have a simple boilerplate/template to clone and quickly start a sclable microservice application.

The service implement 

(Flask, connexion, openAPI, Swagger)

- [Flask](https://github.com/pallets/flask)
- [Flask-Injector](https://pypi.python.org/pypi/Flask-Injector)
- [Connexion](https://github.com/zalando/connexion)


A small microservice API database wrapper

![](img/swagger1.png)

Project Organization
------------

    |
    ├── /account-microservice
    │   ├── /api       
    |   |   ├── __init__.py                         <- Python init file
    |   |   └── accounts.py                         <- Python file where methods are injected in the API
    │   ├── /providers       
    |   |   └── MongoProvider.py                    <- Python file where methods are implemented
    │   ├── /swagger       
    |   |   └── accounts-service-docs.yaml          <- API Swagger file
    │   ├── app.py                                  <- Main python file to run the app
    │   ├── Dockerfile                              <- Dockerfile used to build the image of the microservice
    │   └── requirements.txt                        <- Requirements file with the list of the libraries needed
    │
    ├── /img                                        <- Folder containing the images for this README file
    ├── LICENSE                                     <- License file
    ├── README.md                                   <- This Readme file
    └── docker-compose.yml                          <- Docker compose file, used to run the microservice
     
--------


# Run the microservice
Run the following command in the root folder of the project (need docker and docker-composed installed).
```
docker-compose up
```

# Consult the API documentation
To consult the API documentation just type the following address in a browser.
```
http://localhost:2020/v1.0/ui/
```

**Endpoints available at `http://localhost:2020/v1.0/{URI}`**:

|Method|URI|Description|
|------|---|-----------|
| GET | /accounts/{user_id} | Retrieve data from the DB given an id |
| POST | /accounts/createUser | Insert data into the DB (Any JSON file, id mandatory)|
| PUT | /accounts/updateUser | Update data in the DB |
| DELETE | /accounts/{user_id} | Delete data from the DB | 

# Customize the microservice

To customize the microservice for your own purpose, you have just to modify:
- `MongoProvider.py` This file contains the 
- `accounts.py`
- `accounts-service-docs.yaml` This file contains the [OpenAPI](https://swagger.io/specification/v2/) describing the RESTful API.
Modify this file according to your needs changing paths of the API methods and keeping in mind to modify `parameters`
and `operationId` depending on what you edited in the `accounts.py` file.

# Create New microservices from the boilerplate
To create a new microservice 

Once you have modified re-run the application with the command:
```
docker-compose build && docker-compose up
```