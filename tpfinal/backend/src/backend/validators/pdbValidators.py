import requests
from src.backend.endpoint.endpoints import *


class PdbValidators:

    def __init__(self):
        pass

    @classmethod
    def validate_pdb_code(cls, pdb_code):
        response = requests.get(BASE_URL+'/entry/'+pdb_code)

        response.raise_for_status()

        return response.content
