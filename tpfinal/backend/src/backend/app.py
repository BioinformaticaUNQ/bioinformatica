# coding=utf-8
from flask import Flask, request

from src.backend.service.clustal_service import ClustalService
from src.backend.service.blast_service import BlastService
import json


app = Flask(__name__)

blast_service = BlastService()
clustal_service = ClustalService()


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
