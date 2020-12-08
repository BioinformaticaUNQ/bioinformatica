# coding=utf-8
from flask import Flask, request
from flask_cors import CORS

from src.backend.environment_strategies.environment_strategy import LinuxClustalRunner, WindowsClustalRunner
from src.backend.service.clustal_service import ClustalService
from src.backend.service.blast_service import BlastService
from src.backend.service.dssp_service import DSSPService
from src.backend.service.pdb_service import PDBService
import json


app = Flask(__name__)
CORS(app, suppport_credentials=True)

#clustal_runner = LinuxClustalRunner()
clustal_runner = WindowsClustalRunner()

pdb_service = PDBService()
blast_service = BlastService()
clustal_service = ClustalService(clustal_runner)
dssp_service = DSSPService()


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
    sequence = request.json['sequence']
    covarage = request.json['coverage']
    sequences = blast_service.blast_records(sequence)
    primary_structure = clustal_service.get_alignment_from(sequences)
    chains = sequence.split('|')[1].replace('Chains', '')
    result = dssp_service.get_alignment_from(primary_structure, chains)

    return json.dumps(result)


if __name__ == '__main__':
    app.run()
