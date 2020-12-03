from Bio.Blast import NCBIWWW, NCBIXML
import os
from io import StringIO


def blast_records(id):

    # Primero descubrimos cual es el current working directory
    cwd = os.getcwd()

    # Buscamos donde esta el fasta de la proteina
    fasta_dir = os.path.join(cwd, "fasta")
    fasta = os.path.join(fasta_dir, id+".fasta")

    # Creamos un outfile para ese fasta
    blast_dir = os.path.join(cwd, "blast")
    blast_output = os.path.join(blast_dir, id+"_output.fa")
    with open(blast_output, 'w') as output:
        pass

    # Tenemos "hardcodeado" la base de datos en el proyecto
    db_path = os.path.join(cwd, "db")
    db = os.path.join(db_path, "pdbaa")

    # Hacemos la query a blasta de forma local
    query = "blastp -query {} -out {} -db {}  -evalue {} -outfmt 5".format(
        fasta,
        blast_output,
        db,
        0.001
    )

    os.system(query)

    # Retornamos lo devuelto por blast
    return NCBIXML.parse(open(blast_output))

