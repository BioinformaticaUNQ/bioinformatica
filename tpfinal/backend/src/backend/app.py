# coding=utf-8
from flask import Flask, request

from src.backend.environment_strategies.environment_strategy import LinuxClustalRunner, WindowsClustalRunner
from src.backend.service.clustal_service import ClustalService
from src.backend.service.dssp_service import DSSPService
from src.backend.validators.pdbValidators import PdbValidators
from src.backend.sequence.utils import get_sequence_from
from src.backend.sequence.blastUtils import blast_records


app = Flask(__name__)

CLUSTAL_RUNNER = None

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
    sequences = homologous_sequences_details()
    result = [{'title': seq.get('title'), 'sequence': seq.get('sequence')} for seq in sequences]
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

    # Refactorizar esta shit
    def get_pdb_code(string):
        return ''

    sequences = homologous_sequences_details()

    result = [{'title': seq.get('title'), 'pdbcode': get_pdb_code(seq.get('title')),'sequence': seq.get('sequence')} for seq in sequences]
    c_s = ClustalService(CLUSTAL_RUNNER)
    c_s.get_alignment_from(result)

    dssp_service = DSSPService()
    dssp_service.get_alignment_from(result)


@app.route('/pepe', methods=['GET'])
def pepe():
    return 'Pepe'


if __name__ == '__main__':
    CLUSTAL_RUNNER = LinuxClustalRunner()
    #CLUSTAL_RUNNER = WindowsClustalRunner()
    app.run()
