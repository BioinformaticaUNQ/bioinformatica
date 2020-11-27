from src.backend.services.pdb_service import PdbService
from Bio.Blast import NCBIWWW, NCBIXML

class BlastService:

    def __init__(self):
        self.pdb_service = PdbService()

    def get_homologous_info_from_pdb(self, pdb_code):
        records = self.blast_records(self.pdb_service.get_sequence_from(pdb_code))

        results = []
        for alignment in records.alignments:
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

        return {'d': results}

    def blast_records(self, sequence):
        blast_result = NCBIWWW.qblast(
            "blastp",
            "pdb",
            sequence,
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

        return NCBIXML.read(blast_result)

