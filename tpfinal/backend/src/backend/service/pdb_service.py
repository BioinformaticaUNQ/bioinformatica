
import requests
from src.backend.endpoint.endpoints import *
import os


def get_pdb_code(seqId):
    ''' devuelve el pdb code y el codigo de la cadena. Util en un futuro
        seqId = pdb|2XRG|A
        response (2XRG, A)
    '''
    return (seqId.split('|')[1], seqId.split('|')[2])

def save_fasta_file(id, string_fasta):

    # Encuentro al path asi fasta folder
    dir = os.path.join(os.getcwd(), "fasta\\")

    # Guardo un fasta file en el directorio de fasta
    # con el contenido pasado como argumento
    with open(dir + id + '.fasta', 'w+') as file:
        file.write(string_fasta)


class PDBService:

    """
    Esto podria no ser una clase dado que no tiene colaboradores internos
    pero ya fue es mas facil organizarse asi.
    """

    @classmethod
    def get_pdb_info(cls, pdb_code):
        # Envio request para obtener la informacion almacenada en pdb
        # de la proteina asociado al pdb_code
        response = requests.get(PDB_BASE_URL + '/entry/' + pdb_code)

        # Levanto una exception si la respuesta es algo distinto a 200
        response.raise_for_status()

        # Retorno el contenido de la respuesta parseada
        return response.content.decode("utf-8")

    @classmethod
    def get_sequence_from(cls, pdb_code):

        # Envio la request para obtener el fasta asociado a ese pdb_code
        # en caso que la request haya vuelto con algo distinto a un 200
        # levanta una exception
        fasta_content = ''

        response = requests.get(FASTA_URL.format(pdb_code))
        response.raise_for_status()

        # Parseo contenido del fasta
        fasta_content = response.content.decode("utf-8")

        # Guardo archivo fasta en fasta folder
        save_fasta_file(pdb_code, fasta_content)

        lines = fasta_content.split("\n")[:-1]

        sequences = [lines[i] + "\n" + lines[i + 1] for i in range(0, len(lines), 2)]

        return sequences

