import os
from Bio.Align.Applications import ClustalwCommandline
from Bio import AlignIO
from Bio.Align import MultipleSeqAlignment
from Bio.SeqRecord import SeqRecord



class ClustalService:

    def __init__(self):
        self.fasta_file_name = "analysis.fasta"

    def dump_to_fasta_file(self, sequences):
        fasta_records = ''
        for seq in sequences:
            fasta_records = fasta_records + '>' + seq.get('title') + '\n' + seq.get('sequence') + '\n'

        print(fasta_records)

    def run(self):
        clustalw_exe = 'C:\Program Files (x86)\ClustalW2\clustalw2.exe'
        clustalw_cline = ClustalwCommandline(clustalw_exe, infile=self.fasta_file_path)
        assert os.path.isfile(clustalw_exe), "Clustal W executable missing"
        stdout, stderr = clustalw_cline()


    def _get_alignment(self):
        return AlignIO.read("analysis.aln", "clustal")

    def get_alignment_from(self, sequences):

        self.dump_to_fasta_file(sequences)
        self.run()
        return self._get_alignment()




