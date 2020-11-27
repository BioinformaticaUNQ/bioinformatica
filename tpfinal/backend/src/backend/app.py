# coding=utf-8
from flask import Flask, request
from flask_cors import CORS, cross_origin
from src.backend.validators.pdbValidators import PdbValidators
from src.backend.services.pdb_service import PdbService
from src.backend.services.blast_service import BlastService
app = Flask(__name__)
CORS(app, suppport_credentials=True)

pdb_service = PdbService()
blast_service = BlastService()

@app.route('/pdbCode', methods=['POST'])
@cross_origin(support_credentials=True)
def pdb_code():
    pdb_code = request.json['pdbcode']
    return PdbValidators.validate_pdb_code(pdb_code)


@app.route('/getChoclo', methods=['POST'])
@cross_origin(support_credentials=True)
def choclo():
    pdb_code = request.json['pdbcode']
    return pdb_service.get_sequence_from(pdb_code)


@app.route('/homologousSequence', methods=['POST'])
@cross_origin(support_credentials=True)
def homologous_sequences():
    sequences = homologous_sequences_details()
    result = [{'title': seq.get('title'), 'sequence': seq.get('sequence')} for seq in sequences.get('d')]
    return {'d': result}


@app.route('/homologousSequenceDetails', methods=['POST'])
@cross_origin(support_credentials=True)
def homologous_sequences_details():
    return blast_service.get_homologous_info_from_pdb(request.json['pdbcode'])


if __name__ == '__main__':
    app.run()
