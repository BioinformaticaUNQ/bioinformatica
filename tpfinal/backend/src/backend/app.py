# coding=utf-8
from flask import Flask, request
from flask_cors import CORS, cross_origin
from src.backend.validators.pdbValidators import PdbValidators
import json

app = Flask(__name__)
CORS(app, suppport_credentials=True)


@app.route('/pdbCode', methods=['POST'])
@cross_origin(support_credentials=True)
def pdb_code():
    data = request.form
    PdbValidators.validate_pdb_code(data['pdbcode'])
    return PdbValidators.validate_pdb_code(data['pdbcode'])


if __name__ == '__main__':
    app.run()
