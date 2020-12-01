import os
from Bio.Align.Applications import ClustalwCommandline
from Bio import AlignIO
from Bio.Align import MultipleSeqAlignment
from Bio.SeqRecord import SeqRecord
from constants.constants import clustalw


class ClustalService:

    def __init__(self):
        self.file_name = "analyze"

    def _file(self, extension):
        return self.file_name + '.'+ extension

    def dump_to_fasta_file(self, sequences):
        fasta_records = ''
        for seq in sequences:
            fasta_records = fasta_records + '>' + seq.get('title') + '\n' + seq.get('sequence') + '\n'

        with open(self._file('fasta'), "w") as text_file:
            text_file.write(fasta_records)

    def run(self):

        clustalw_cline = ClustalwCommandline(clustalw, infile=self._file('fasta'))
        #assert os.path.isfile(clustalw), "Clustal W executable missing"
        stdout, stderr = clustalw_cline()


    def _get_alignment(self):
        return AlignIO.read(self._file('aln'), "clustal")

    def get_alignment_from(self, sequences):

        self.dump_to_fasta_file(sequences)
        self.run()
        return self._get_alignment()




