import os

from Bio import AlignIO
from Bio.Align import MultipleSeqAlignment
from Bio.SeqRecord import SeqRecord


class ClustalService:

    def __init__(self, clustal_runner):
        self.file_name = "../files/clustal/analyze"
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
        return [seq.seq.__str__() for seq in AlignIO.read(self._file('aln'), "clustal")]

    def get_alignment_from(self, sequences):

        self.dump_to_fasta_file(sequences)
        self.run()
        return self._get_alignment()




