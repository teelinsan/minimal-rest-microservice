import os
from flask_injector import inject
from providers.MongoProvider import MongoProvider

data_provider = MongoProvider()

@inject
def create_user(user_payload):
    return data_provider.create_user(user_payload)

@inject
def read_user(user_id):
    return data_provider.read_user(user_id)

@inject
def update_user(user_payload):
    return data_provider.update_user(user_payload)

@inject
def delete_user(user_id):
    return data_provider.delete_user(user_id)


def basic_auth(username, password, required_scopes=None):
    if username == os.environ.get('ADMIN_USERNAME', 'admin') and password == os.environ.get('ADMIN_PASSWORD', 'password'):
        return {'sub': 'admin'}
    # optional: raise exception for custom error response
    return None
