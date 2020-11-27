import requests
from src.backend.endpoint.endpoints import *


class Sequences:

    def __init__(self):
        pass

    @classmethod
    def sequence(cls, pdb_code):
        response = requests.get(BASE_URL + '/sequence/' + pdb_code)

        response.raise_for_status()

        return response.content
