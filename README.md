# Minimal REST API Microservice Boilerplate

A minimal REST API microservice in python.

(Flask, connexion, openAPI, Swagger)

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

# Customize the microservice