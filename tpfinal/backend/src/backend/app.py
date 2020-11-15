# coding=utf-8
from flask import Flask, request
from flask_cors import CORS, cross_origin
from src.backend.validators.pdbValidators import PdbValidators
from src.backend.sequence.utils import get_sequence_from
from src.backend.sequence.blastUtils import blast_records
import json

app = Flask(__name__)
CORS(app, suppport_credentials=True)

@app.route('/pdbCode', methods=['POST'])
@cross_origin(support_credentials=True)
def pdb_code():
    data = request.form
    PdbValidators.validate_pdb_code(data['pdbcode'])
    return PdbValidators.validate_pdb_code(data['pdbcode'])


@app.route('/sequence', methods=['POST'])
@cross_origin(support_credentials=True)
def sequence():
    pdb_code = request.form['pdbcode']
    PdbValidators.validate_pdb_code(pdb_code)

    return get_sequence_from(pdb_code) if PdbValidators.validate_pdb_code(pdb_code) else ''

@app.route('/homologousSequence', methods=['POST'])
@cross_origin(support_credentials=True)
def homologous_sequences():
    sequences = homologous_sequences_details()
    result = [{'title': seq.get('title'), 'sequence': seq.get('sequence')} for seq in sequences.get('d')]
    return {'d': result}

@app.route('/homologousSequenceDetails', methods=['POST'])
@cross_origin(support_credentials=True)
def homologous_sequences_details():
    main_sequence = sequence();
    print(main_sequence)

    records = blast_records(main_sequence)

    results = []
    for alignment in records.alignments:
        aligmened_sequence = ''
        aligmened_matches = ''
        for hsp in alignment.hsps:
            aligmened_sequence = aligmened_sequence + hsp.sbjct
            aligmened_matches = aligmened_matches + hsp.match

        results.append({
            'title': alignment.title.split('>')[0],
            'sequence' : aligmened_sequence.replace('-', ''),
            'aligmened_matches': aligmened_matches,
            'aligmened_sequence': aligmened_sequence
        })

    return {'d': results}


if __name__ == '__main__':
    app.run()
