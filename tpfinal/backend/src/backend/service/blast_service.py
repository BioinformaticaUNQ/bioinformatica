from Bio.Blast import NCBIXML
import os
from src.backend.service.pdb_service import save_fasta_file, PDBService

minimun_identity_expected = 40

class BlastService:

    """
        Esto podria no ser una clase dado que no tiene colaboradores internos
        pero ya fue es mas facil organizarse asi.
    """

    def blast_records(self, fasta_sequence, evalue=0.001, gapopen=11, gapextend=1, matrix='BLOSUM62', expected_coverage=90):
        # Me quedo con el id y con la secuencia
        pdb_code, sequence = fasta_sequence.split("\n")
        pdb_code = pdb_code.split("|")[0][1:5]

        save_fasta_file(pdb_code, fasta_sequence)

        # Obtengo todos los paths necesarios para realizar nuestra query local
        fasta, blast_output, db = self.create_paths(pdb_code)

        # Hacemos query de forma local
        self.query_to_local_blast(fasta, blast_output, db, evalue, gapopen, gapextend, matrix)

        # Parseamos lo devuelto por blast
        records = NCBIXML.parse(open(blast_output))

        # Retornamos "todas" las secuencias homologas a la secuencia original
        return self.parse_records_to_sequences(records, len(sequence), expected_coverage)

    def query_to_local_blast(self, fasta, blast_output, db, evalue=0.001,  gapopen=11, gapextend=1, matrix='BLOSUM62'):
        # Hacemos la query a blasta de forma local
        query = "blastp -query {} -out {} -db {}  -evalue {} -gapopen {} -gapextend {} -matrix {} -outfmt 5".format(
            fasta,
            blast_output,
            db,
            evalue,
            gapopen,
            gapextend,
            matrix
        )

        os.system(query)

    def create_paths(self, pdb_code):
        # Primero descubrimos cual es el current working directory
        cwd = os.getcwd()

        # Buscamos donde esta el fasta de la proteina
        fasta_dir = os.path.join(cwd, "fasta")
        fasta = os.path.join(fasta_dir, pdb_code + ".fasta")

        # Creamos un outfile para ese fasta
        blast_dir = os.path.join(cwd, "blast")
        blast_output = os.path.join(blast_dir, pdb_code + "_output.fa")
        with open(blast_output, 'w') as output:
            pass

        # Tenemos "hardcodeado" la base de datos en el proyecto
        db_path = os.path.join(cwd, "db")
        db = os.path.join(db_path, "pdbaa")

        return fasta, blast_output, db

    def parse_records_to_sequences(self, records, query_len, coverage_expected):
        results = []
        for record in records:
            for alignment in record.alignments:
                if self.is_identity_and_coverage_valid(alignment, query_len, coverage_expected) :
                    try:
                        results.append({
                            'title': alignment.title.split('>')[0],
                            'sequence': PDBService.get_sequence(alignment.hit_id.split('|')[1], alignment.hit_id.split('|')[2])
                        })
                    except:
                        print('secuencia ignorada por error en pbdserivce.')
                else:
                    print(alignment.hit_id.split('|')[1], 'filtered')

    def is_identity_and_coverage_valid(self, alignment, query_len, coverage_expected):

        # seq.alignments[1].hsps[0]
        hsps_of_sequence = alignment.hsps[0]
        identity = hsps_of_sequence.identities
        query_to = hsps_of_sequence.query_end
        query_from = hsps_of_sequence.query_start
        return self.identity_greater_than(identity) and \
               self.coverage_greater_than(query_to, query_from, query_len, coverage_expected)

    def identity_greater_than(self, identity):
        return minimun_identity_expected < identity

    @staticmethod
    def coverage_greater_than(query_to, query_from, query_len, coverage_expected):
        coverage = (query_to - query_from) / query_len
        print('Coverage:', coverage * 100)
        return (coverage * 100) >= coverage_expected

    def blast_records_just_sequences(self, fasta_sequence):
        sequences = self.blast_records(fasta_sequence)

        result = [{'title': seq.get('title'), 'sequence': seq.get('sequence')} for seq in sequences]

        return result