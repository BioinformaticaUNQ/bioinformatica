from Bio.Blast import NCBIWWW, NCBIXML
import os

def blast_records(sequence):
    blast_result = NCBIWWW.qblast(program="blastp",
                                  database="pdb",
                                  sequence=sequence,
                                  expect=0.01)

    return NCBIXML.read(blast_result)

def copy_blast_records():
    fasta = 'C:/Users/tumba/OneDrive/Desktop/bioinformatica/tpfinal/backend/src/backend/fasta/1MCY.fasta'
    out_put = 'C:/Users/tumba/OneDrive/Desktop/bioinformatica/tpfinal/backend/src/backend/blast/output.fa'
    db = 'C:/Program Files/NCBI/blast-2.11.0+/db/pdbaa'

    query = "blastp -query {} -out {} -db {}".format(
        fasta,
        out_put,
        db
    )
    print(s)
    os.system(s)