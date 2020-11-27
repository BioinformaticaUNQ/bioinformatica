from Bio.Blast import NCBIWWW, NCBIXML


def blast_records(sequence):
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
