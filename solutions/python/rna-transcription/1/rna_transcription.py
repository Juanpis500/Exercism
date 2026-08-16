"""
    In this module exist a function that implement the solucion of th RNA transciption.
"""


def to_rna(dna_strand):
    """ RNA Transciption
        Parameter:
            dnq_strand(string): The DNA sequence.
        Return:
            rna_complement(string): The transcription of the DNA squence given.
    """
    rna_complement = ''
    pairs = {'G':'C', 'C':'G', 'T':'A', 'A':'U'}

    for dna in dna_strand:
        rna_complement += pairs.get(dna)

    return rna_complement