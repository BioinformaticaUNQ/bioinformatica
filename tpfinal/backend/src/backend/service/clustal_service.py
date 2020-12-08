from Bio import AlignIO
from src.backend.service.pdb_service import get_pdb_code
#from Bio.Align import MultipleSeqAlignment
#from Bio.SeqRecord import SeqRecord


class ClustalService:

    def __init__(self, clustal_runner):
        self.file_name = "./clustal/analyze"
        self.clustal_runner = clustal_runner

    def _file(self, extension):
        return self.file_name + '.'+ extension

    def dump_to_fasta_file(self, sequences):
        fasta_records = ''
        for seq in sequences:
            fasta_records = fasta_records + '>' + seq.get('title') + '\n' + seq.get('sequence') + '\n'

        with open(self._file('fasta'), "w") as text_file:
            text_file.write(fasta_records)

    def run(self):
        self.clustal_runner.run(self._file('fasta'))

    def _get_alignment(self):
        c = AlignIO.read(self._file('aln'), "clustal")
        return [self._create_record_alignment(seq) for seq in c]

    def _create_record_alignment(self, aligmentedSequence):
        return {
            'pdbcode': get_pdb_code(aligmentedSequence.id)[0],
            'sequence': aligmentedSequence.seq.__str__(),
            'chains': get_pdb_code(aligmentedSequence.id)[1]
        }

    def get_alignment_from(self, sequences):

        self.dump_to_fasta_file(sequences)
        self.run()
        return self._get_alignment()




