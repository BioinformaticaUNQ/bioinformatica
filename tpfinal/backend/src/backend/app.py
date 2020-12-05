# coding=utf-8
from flask import Flask, request

from src.backend.service.clustal_service import ClustalService
from src.backend.service.blast_service import BlastService
from src.backend.service.pdb_service import PDBService
import json


app = Flask(__name__)

pdb_service = PDBService()
blast_service = BlastService()
clustal_service = ClustalService()


@app.route('/sequences', methods=['POST'])
def getSequences():
    pdb_code = request.json['pdbcode']

    result = pdb_service.get_sequence_from(pdb_code)

    return json.dumps(result)


@app.route('/homologousSequence', methods=['POST'])
def homologous_sequences():
    pdb_code = request.json['pdbcode']

    result = blast_service.blast_records_just_sequences(pdb_code)

    return json.dumps(result)


@app.route('/analyze', methods=['POST'])
def analyze():
    pdb_code = request.json['pdbcode']
    sequences = blast_service.blast_records(pdb_code)

    return clustal_service.get_alignment_from(sequences)


if __name__ == '__main__':
    app.run()
