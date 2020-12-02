from Bio.PDB import PDBList
from Bio.PDB.DSSP import dssp_dict_from_pdb_file

class DSSPService:

    def get_alignment_from(self, sequences):
        return [self._get_alignment(sequence) for sequence in sequences]

    def _get_alignment(self, sequence):
        pdbcode = sequence.get('pdbcode')
        self._generate_pdb(pdbcode)
        return self._run(pdbcode)

    def _generate_pdb(self, pdbcode):
        # Esto se puede poner en el pdb service
        pdbl = PDBList()
        pdbl.retrieve_pdb_file(pdbcode, pdir='../files/pdb', file_format='pdb')

    def _run(self, pdbcode):
        pdb_file = pdbcode + '.pdb'
        return dssp_dict_from_pdb_file(pdb_file, outfile=pdbcode, outext='_dssp.df' )