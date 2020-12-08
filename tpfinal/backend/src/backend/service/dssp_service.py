from Bio.PDB import PDBList
from Bio.PDB.DSSP import dssp_dict_from_pdb_file
from Bio.PDB.DSSP import DSSP
from Bio.PDB import PDBParser
import queue


PDB_PATH = './pdb/'
class DSSPService:

    def get_alignment_from(self, sequences, chains):
        return [{'dssp' : self._get_alignment(sequence, chains), 'sequence' : sequence} for sequence in sequences]
        #return (self._get_alignment(sequences[3], chains), sequences[3])

    def _get_alignment(self, sequence, expectede_chains):
        pdbcode = sequence.get('pdbcode').lower()
        self._generate_pdb(pdbcode)
        secondary_structure =  self._run(pdbcode, sequence.get('chains'))
        return self._align(secondary_structure, sequence.get('sequence'))

    def _align(self, secondary_structure, alignmed_primary_structure):

        for index in range(len(alignmed_primary_structure)):
            if alignmed_primary_structure[index] == '-':
                secondary_structure.insert(index, (1, '-', '_'))

        r = ''.join([st[2] for st in secondary_structure])
        return r

    def _generate_pdb(self, pdbcode):
        pdbl = PDBList()
        r = pdbl.retrieve_pdb_file(pdbcode, pdir=PDB_PATH, file_format='pdb', overwrite=True)

    def _run(self, pdbcode, chains):
        pdb_file = PDB_PATH + 'pdb' + pdbcode + '.ent'
        #return dssp_dict_from_pdb_file(pdb_file, DSSP="dssp")
        p = PDBParser()
        structure = p.get_structure(pdbcode, pdb_file)
        model = structure[0]
        dssp = DSSP(model, pdb_file)
        valid_keys = [key for key in dssp.keys() if key[0] in chains]
        return [ dssp[key] for key in valid_keys]