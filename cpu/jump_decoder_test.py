import pytest
from jump_decoder import JumpDecoder

jump_decoder = JumpDecoder()

def test_jump_decoder():

    alu_out = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    j1 = 0
    j2 = 0
    j3 = 0
    load = jump_decoder.compute(alu_out, j1, j2, j3)
    assert load == 0

    alu_out = [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    j1 = 0
    j2 = 0
    j3 = 0
    load = jump_decoder.compute(alu_out, j1, j2, j3)
    assert load == 0

    alu_out = [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    j1 = 0
    j2 = 0
    j3 = 0
    load = jump_decoder.compute(alu_out, j1, j2, j3)
    assert load == 0

    alu_out = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    j1 = 0
    j2 = 0
    j3 = 1
    load = jump_decoder.compute(alu_out, j1, j2, j3)
    assert load == 1

    alu_out = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    j1 = 0
    j2 = 0
    j3 = 1
    load = jump_decoder.compute(alu_out, j1, j2, j3)
    assert load == 0

    alu_out = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    j1 = 0
    j2 = 0
    j3 = 1
    load = jump_decoder.compute(alu_out, j1, j2, j3)
    assert load == 0

    alu_out = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    j1 = 0
    j2 = 1
    j3 = 0
    load = jump_decoder.compute(alu_out, j1, j2, j3)
    assert load == 1

    alu_out = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    j1 = 0
    j2 = 1
    j3 = 0
    load = jump_decoder.compute(alu_out, j1, j2, j3)
    assert load == 0

    alu_out = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1]
    j1 = 0
    j2 = 1
    j3 = 0
    load = jump_decoder.compute(alu_out, j1, j2, j3)
    assert load == 0

    alu_out = [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0]
    j1 = 0
    j2 = 1
    j3 = 1
    load = jump_decoder.compute(alu_out, j1, j2, j3)
    assert load == 1

    alu_out = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    j1 = 0
    j2 = 1
    j3 = 1
    load = jump_decoder.compute(alu_out, j1, j2, j3)
    assert load == 1

    alu_out = [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    j1 = 0
    j2 = 1
    j3 = 1
    load = jump_decoder.compute(alu_out, j1, j2, j3)
    assert load == 0

    alu_out = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    j1 = 1
    j2 = 0
    j3 = 0
    load = jump_decoder.compute(alu_out, j1, j2, j3)
    assert load == 1

    alu_out = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    j1 = 1
    j2 = 0
    j3 = 0
    load = jump_decoder.compute(alu_out, j1, j2, j3)
    assert load == 0

    alu_out = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1]
    j1 = 1
    j2 = 0
    j3 = 0
    load = jump_decoder.compute(alu_out, j1, j2, j3)
    assert load == 0

    alu_out = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    j1 = 1
    j2 = 0
    j3 = 1
    load = jump_decoder.compute(alu_out, j1, j2, j3)
    assert load == 1

    alu_out = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    j1 = 1
    j2 = 0
    j3 = 1
    load = jump_decoder.compute(alu_out, j1, j2, j3)
    assert load == 1

    alu_out = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    j1 = 1
    j2 = 0
    j3 = 1
    load = jump_decoder.compute(alu_out, j1, j2, j3)
    assert load == 0

    alu_out = [1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    j1 = 1
    j2 = 1
    j3 = 0
    load = jump_decoder.compute(alu_out, j1, j2, j3)
    assert load == 1

    alu_out = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    j1 = 1
    j2 = 1
    j3 = 0
    load = jump_decoder.compute(alu_out, j1, j2, j3)
    assert load == 1

    alu_out = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    j1 = 1
    j2 = 1
    j3 = 0
    load = jump_decoder.compute(alu_out, j1, j2, j3)
    assert load == 0
