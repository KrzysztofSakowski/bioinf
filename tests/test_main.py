from main import gplmDCA_asymmetric

def test_sequence():
    gplmDCA_asymmetric('fasta.fas','output.out', 0.01, 0.01, 0.01, 0.1, 2, -1)