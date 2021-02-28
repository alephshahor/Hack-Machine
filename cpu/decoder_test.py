import pytest

from decoder import Decoder

decoder = Decoder()

instructions = [
    [0, 0, 0, 0,  0, 0, 0, 0,  0, 0, 0, 1,  0, 0, 0, 0],
    [1, 1, 1, 0,  1, 1, 1, 1,  1, 1, 0, 0,  0, 0, 0, 0],
    [0, 0, 0, 0,  0, 0, 0, 0,  0, 0, 0, 1,  0, 0, 0, 1],
    [1, 1, 1, 0,  1, 0, 1, 0,  1, 0, 0, 1,  1, 0, 0, 0],
    [0, 0, 0, 0,  0, 0, 0, 0,  0, 0, 0, 1,  0, 0, 0, 0],
    [1, 1, 1, 1,  1, 1, 0, 0,  0, 0, 0, 1,  0, 0, 0, 0],
    [0, 0, 0, 0,  0, 0, 0, 0,  0, 1, 1, 0,  0, 0, 0, 0],
    [1, 1, 1, 0,  0, 1, 0, 0,  1, 1, 0, 1,  0, 0, 0, 0],
    [0, 0, 0, 0,  0, 0, 0, 0,  0, 0, 0, 1,  0, 0, 1, 0],
    [1, 1, 1, 0,  0, 0, 1, 1,  0, 0, 0, 0,  0, 0, 0, 1],
    [0, 0, 0, 0,  0, 0, 0, 0,  0, 0, 0, 1,  0, 0, 0, 0],
]

def test_decoder():
    for instr in instructions:
        x, a, c1, c2, c3, c4, c5, c6, d1, d2, d3, j1, j2, j3 = decoder.compute(instr)
        assert x == instr[0], 'Expected x to be {} but got {}'.format(instr[0], x)
        assert a == instr[3], 'Expected a to be {} but got {}'.format(instr[3], a)
        assert c1 == instr[4], 'Expected c1 to be {} but got {}'.format(instr[4], c1)
        assert c2 == instr[5], 'Expected c2 to be {} but got {}'.format(instr[5], c2)
        assert c3 == instr[6], 'Expected c3 to be {} but got {}'.format(instr[6], c3)
        assert c4 == instr[7], 'Expected c4 to be {} but got {}'.format(instr[7], c4)
        assert c5 == instr[8], 'Expected c5 to be {} but got {}'.format(instr[8], c5)
        assert c6 == instr[9], 'Expected c6 to be {} but got {}'.format(instr[9], c6)
        assert d1 == instr[10], 'Expected d1 to be {} but got {}'.format(instr[10], d1)
        assert d2 == instr[11], 'Expected d2 to be {} but got {}'.format(instr[11], d2)
        assert d3 == instr[12], 'Expected d3 to be {} but got {}'.format(instr[12], d3)
        assert j1 == instr[13], 'Expected j1 to be {} but got {}'.format(instr[13], j1)
        assert j2 == instr[14], 'Expected j2 to be {} but got {}'.format(instr[14], j2)
        assert j3 == instr[15], 'Expected j3 to be {} but got {}'.format(instr[15], j3)
