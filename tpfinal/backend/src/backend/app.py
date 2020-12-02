# coding=utf-8
from flask import Flask, request

from src.backend.service.clustal_service import ClustalService
from src.backend.validators.pdbValidators import PdbValidators
from src.backend.sequence.utils import get_sequence_from
from src.backend.sequence.blastUtils import blast_records


app = Flask(__name__)



@app.route('/pdbCode', methods=['POST'])

def pdb_code():
    pdb_code = request.json['pdbcode']
    return PdbValidators.validate_pdb_code(pdb_code)


@app.route('/sequence', methods=['POST'])

def sequence():
    pdb_code = request.form['pdbcode']
    return get_sequence_from(pdb_code) if PdbValidators.validate_pdb_code(pdb_code) else ''


@app.route('/homologousSequence', methods=['POST'])

def homologous_sequences():
    print('Entered')
    sequences = homologous_sequences_details()
    result = [{'title': seq.get('title'), 'sequence': seq.get('sequence')} for seq in sequences.get('d')]
    return {'d': result}

@app.route('/homologousSequenceDetails', methods=['POST'])

def homologous_sequences_details():
    main_sequence = sequence()
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

    return results

@app.route('/analyze', methods=['POST'])
def analyze():
    sequences = homologous_sequences_details()

    result = [{'title': seq.get('title'), 'sequence': seq.get('sequence')} for seq in sequences]
    c_s = ClustalService()
    return {'d': c_s.get_alignment_from(result)}


@app.route('/pepe', methods=['GET'])
def pepe():
    return 'Pepe'


if __name__ == '__main__':
    app.run()
