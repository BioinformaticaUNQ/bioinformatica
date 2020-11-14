import requests


def get_sequence_from(pdbid):
    base_url = 'https://www.rcsb.org/fasta/entry/{}/download'.format(pdbid)
    response = requests.get(base_url)

    byte_content = response.content
    fasta_content = byte_content.decode("utf-8")

    return fasta_content.split('\n')[1]
