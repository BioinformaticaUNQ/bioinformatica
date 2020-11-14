# coding=utf-8
from flask import Flask, request
from flask_cors import CORS, cross_origin
from src.backend.validators.pdbValidators import PdbValidators
from src.backend.sequence.utils import get_sequence_from
import json

from Bio.Blast import NCBIWWW, NCBIXML

app = Flask(__name__)
CORS(app, suppport_credentials=True)

@app.route('/pdbCode', methods=['POST'])
@cross_origin(support_credentials=True)
def pdb_code():
    data = request.form
    PdbValidators.validate_pdb_code(data['pdbcode'])
    return PdbValidators.validate_pdb_code(data['pdbcode'])


@app.route('/sequence', methods=['POST'])
def sequence():
    pdb_code = request.form['pdbcode']
    PdbValidators.validate_pdb_code(pdb_code)
    sequence = ''

    if PdbValidators.validate_pdb_code(pdb_code):
        sequence = get_sequence_from(pdb_code)

    print(sequence)
    return sequence

@app.route('/homologousSequence', methods=['POST'])
def homologous_sequences():
    main_sequence = sequence();

    blast_result_1 = NCBIWWW.qblast(
        "blastp",
        "pdb",
        main_sequence,
        short_query=True,
        hitlist_size=50,
        expect=1000,
        word_size=7,
        nucl_reward=1,
        matrix_name='BLOSUM62',
        nucl_penalty=-3,
        threshold=0.05,
        gapcosts="11 1",
    )

    blast_records = NCBIXML.read(blast_result_1)
    for alignment in blast_records.alignments:
        for hsp in alignment.hsps:
            print(hsp)

    return 'Yeap'


if __name__ == '__main__':
    app.run()
