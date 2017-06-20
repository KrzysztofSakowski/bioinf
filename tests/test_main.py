from main import gplmDCA_asymmetric

def test_sequence():
    gplmDCA_asymmetric('fasta_short.fas','output.out', 0.01, 0.01, 0.01, 0.1, 1, 2)