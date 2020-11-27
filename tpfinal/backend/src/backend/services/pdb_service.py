import requests
from src.backend.endpoint.endpoints import *


class PdbService:

    def get_info_from_pdb(self, pdb_code):
        response = requests.get(BASE_URL + '/entry/' + pdb_code)

        response.raise_for_status()

        return response.content

    def get_sequence_from(self, pdb_code):
        base_url = FASTA_URL + '{}/download' .format(pdb_code)
        response = requests.get(base_url)
        response.raise_for_status()
        byte_content = response.content
        fasta_content = byte_content.decode("utf-8")

        return fasta_content.split('\n')[1]
