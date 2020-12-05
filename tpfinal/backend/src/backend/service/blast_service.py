from Bio.Blast import NCBIXML
import os
from src.backend.service.pdb_service import PDBService


class BlastService:

    """
        Esto podria no ser una clase dado que no tiene colaboradores internos
        pero ya fue es mas facil organizarse asi.
    """

    def blast_records(self, pdb_code):
        # Genero el archivo fasta en nuestra fasta folder
        PDBService().get_sequence_from(pdb_code)

        # Obtengo todos los paths necesarios para realizar nuestra query local
        fasta, blast_output, db = self.create_paths(pdb_code)

        # Hacemos query de forma local
        self.query_to_local_blast(fasta, blast_output, db)

        # Parseamos lo devuelto por blast
        records = NCBIXML.parse(open(blast_output))

        # Retornamos "todas" las secuencias homologas a la secuencia original
        return self.parse_records_to_sequences(records)

    def query_to_local_blast(self, fasta, blast_output, db):
        # Hacemos la query a blasta de forma local
        query = "blastp -query {} -out {} -db {}  -evalue {} -outfmt 5".format(
            fasta,
            blast_output,
            db,
            0.001
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

    def parse_records_to_sequences(self, records):

        results = []
        for record in records:
            for alignment in record.alignments:
                aligmened_sequence = ''
                aligmened_matches = ''
                for hsp in alignment.hsps:
                    aligmened_sequence = aligmened_sequence + hsp.sbjct
                    aligmened_matches = aligmened_matches + hsp.match

                results.append({
                    'title': alignment.title.split('>')[0],
                    'sequence': aligmened_sequence.replace('-', ''),
                    'aligmened_matches': aligmened_matches,
                    'aligmened_sequence': aligmened_sequence
                })

        return results

    def blast_records_just_sequences(self, pdb_code):
        sequences = self.blast_records(pdb_code)

        result = [{'title': seq.get('title'), 'sequence': seq.get('sequence')} for seq in sequences]

        return result