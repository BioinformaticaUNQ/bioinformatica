import requests
import os
from Bio.PDB import PDBList
def get_sequence_from(pdbid):
    base_url = 'https://www.rcsb.org/fasta/entry/{}/download'.format(pdbid)
    response = requests.get(base_url)

    byte_content = response.content

    fasta_content = byte_content.decode("utf-8")

    save_fasta_file(pdbid, fasta_content)

    return fasta_content.split('\n')[1]


def save_fasta_file(id, string_fasta):
    dir = os.path.join(os.getcwd(), "fasta\\")

    with open(dir+id+'.fasta', 'w+') as file:
        file.write(string_fasta)
