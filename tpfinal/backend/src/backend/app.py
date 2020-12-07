# coding=utf-8
from flask import Flask, request

from src.backend.environment_strategies.environment_strategy import LinuxClustalRunner, WindowsClustalRunner
from src.backend.service.clustal_service import ClustalService
from src.backend.service.blast_service import BlastService
from src.backend.service.pdb_service import PDBService
from flask_cors import CORS, cross_origin
import json


app = Flask(__name__)
CORS(app, suppport_credentials=True)

clustal_runner = LinuxClustalRunner()
#clustal_runner = WindowsClustalRunner()

pdb_service = PDBService()
blast_service = BlastService()
clustal_service = ClustalService(clustal_runner)


@app.route('/sequences', methods=['POST'])
@cross_origin(support_credentials=True)
def getSequences():
    pdb_code = request.json['pdbcode']

    result = pdb_service.get_sequence_from(pdb_code)

    return json.dumps(result)


@app.route('/homologousSequence', methods=['POST'])
@cross_origin(support_credentials=True)
def homologous_sequences():
    sequence = request.json['sequence']

    result = blast_service.blast_records_just_sequences(sequence)

    return json.dumps(result)


@app.route('/analyze', methods=['POST'])
@cross_origin(support_credentials=True)
def analyze():
    sequence = request.json['sequence']
    sequences = blast_service.blast_records(sequence)
    result = clustal_service.get_alignment_from(sequences)

    return json.dumps(result)


if __name__ == '__main__':
    app.run()
