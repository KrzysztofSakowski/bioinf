from Bio.Seq import Seq
from Bio.Alphabet import IUPAC


def test_sequence():
    seq = Seq("AUAU", IUPAC.unambiguous_dna)
    assert seq.count("A") == seq.count("U")


def test_sequence_2():
    seq = Seq("AUAUA", IUPAC.unambiguous_dna)
    assert seq.count("A") != seq.count("U")
