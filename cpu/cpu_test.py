import pytest
import sys
import os

sys.path.append(os.environ['ROOT_FOLDER'] + '/utils')
import conversions

from cpu import CPU

cpu = CPU()
zero = [0] * 16
one = zero[:15] + [1]
n_bit = 16

instructions = [
    [0, 0, 0, 0,  0, 0, 0, 0,  0, 0, 0, 1,  0, 0, 0, 0], # @i
    [1, 1, 1, 0,  1, 1, 1, 1,  1, 1, 0, 0,  1, 0, 0, 0], # M=1
    [0, 0, 0, 0,  0, 0, 0, 0,  0, 0, 0, 1,  0, 0, 0, 1], # @sum
    [1, 1, 1, 0,  1, 0, 1, 0,  1, 0, 0, 1,  1, 0, 0, 0], # M=0
    [0, 0, 0, 0,  0, 0, 0, 0,  0, 0, 0, 1,  0, 0, 0, 0], # @i
    [1, 1, 1, 1,  1, 1, 0, 0,  0, 0, 0, 1,  0, 0, 0, 0], # D=M
    [0, 0, 0, 0,  0, 0, 0, 0,  0, 1, 1, 0,  0, 1, 0, 0], # @100
    [1, 1, 1, 0,  0, 1, 0, 0,  1, 1, 0, 1,  0, 0, 0, 0], # D=D-A
    [0, 0, 0, 0,  0, 0, 0, 0,  0, 0, 0, 1,  0, 0, 1, 0], # @END
    [1, 1, 1, 0,  0, 0, 1, 1,  0, 0, 0, 0,  0, 0, 0, 1], # D;JGT
    [0, 0, 0, 0,  0, 0, 0, 0,  0, 0, 0, 1,  0, 0, 0, 0], # @i
    [1, 1, 1, 1,  1, 1, 0, 0,  0, 0, 0, 1,  0, 0, 0, 0], # D=M
    [0, 0, 0, 0,  0, 0, 0, 0,  0, 0, 0, 1,  0, 0, 0, 1], # @sum
    [1, 1, 1, 1,  0, 0, 0, 0,  1, 0, 0, 0,  1, 0, 0, 0], # M=D+M
    [0, 0, 0, 0,  0, 0, 0, 0,  0, 0, 0, 1,  0, 0, 0, 0], # @i
    [1, 1, 1, 1,  1, 1, 0, 1,  1, 1, 0, 0,  1, 0, 0, 0], # M=M+1
    [0, 0, 0, 0,  0, 0, 0, 0,  0, 0, 0, 0,  0, 1, 0, 0], # @LOOP
    [1, 1, 1, 0,  1, 0, 1, 0,  1, 0, 0, 0,  0, 1, 1, 1], # 0;JMP
    [0, 0, 0, 0,  0, 0, 0, 0,  0, 0, 0, 1,  0, 0, 1, 0], # @END
    [1, 1, 1, 0,  1, 0, 1, 0,  1, 0, 0, 0,  0, 1, 1, 1], # 0;JMP
]

# COMPROBAR TODAS LAS VARIABLES INTERNAS!!
def test_cpu():

    instr = instructions[0] # @i
    mem_in = zero

    alu_out, load_pc, mem_dir = cpu.compute(instr, mem_in)

    # assert cpu.load_pc == 0
    assert cpu.a_register.value() == conversions.dec_to_bin_arr(n_bit, 16)
    assert cpu.d_register.value() == zero
    assert alu_out == zero
    assert load_pc == 0
    assert mem_dir == zero

    instr = instructions[1] # M=1
    mem_in = zero

    alu_out, load_pc, mem_dir = cpu.compute(instr, mem_in)

    assert cpu.jump_decoder_out == 0
    assert cpu.a_register.value() == conversions.dec_to_bin_arr(n_bit, 16)
    assert cpu.d_register.value() == zero
    assert alu_out == conversions.dec_to_bin_arr(n_bit, 1)
    assert load_pc == 0
    assert mem_dir == conversions.dec_to_bin_arr(n_bit, 16)

    instr = instructions[2] # @sum
    mem_in = conversions.dec_to_bin_arr(n_bit, 1)
    alu_out, load_pc, mem_dir = cpu.compute(instr, mem_in)


    assert cpu.a_register.value() == conversions.dec_to_bin_arr(n_bit, 17)
    assert cpu.d_register.value() == zero
    assert load_pc == 0
    assert mem_dir == conversions.dec_to_bin_arr(n_bit, 16)


    instr = instructions[3] # M=0
    mem_in = conversions.dec_to_bin_arr(n_bit, 0)
    alu_out, load_pc, mem_dir = cpu.compute(instr, mem_in)

    assert cpu.jump_decoder_out == 0
    assert cpu.a_register.value() == conversions.dec_to_bin_arr(n_bit, 17)
    assert cpu.d_register.value() == zero
    assert load_pc == 0
    assert alu_out == zero
    assert mem_dir == conversions.dec_to_bin_arr(n_bit, 17)

    sum_ = 0

    # (LOOP)

    for i in range(100):

        instr = instructions[4] # @i
        mem_in = conversions.dec_to_bin_arr(n_bit, 0)
        alu_out, load_pc, mem_dir = cpu.compute(instr, mem_in)

        assert cpu.a_register.value() == conversions.dec_to_bin_arr(n_bit, 16)
        assert cpu.d_register.value() == conversions.dec_to_bin_arr(n_bit, i)
        assert load_pc == 0
        if i == 0:
            assert mem_dir == conversions.dec_to_bin_arr(n_bit, 17)
        else:
            assert mem_dir == conversions.dec_to_bin_arr(n_bit, 4)

        instr = instructions[5] # D = M
        mem_in = conversions.dec_to_bin_arr(n_bit, i + 1)
        alu_out, load_pc, mem_dir = cpu.compute(instr, mem_in)

        assert cpu.jump_decoder_out == 0
        assert cpu.a_register.value() == conversions.dec_to_bin_arr(n_bit, 16)
        assert cpu.d_register.value() == conversions.dec_to_bin_arr(n_bit, i + 1)
        assert load_pc == 0
        assert alu_out == conversions.dec_to_bin_arr(n_bit, i + 1)
        assert mem_dir == conversions.dec_to_bin_arr(n_bit, 16)

        instr = instructions[6]  # @100
        mem_in = conversions.dec_to_bin_arr(n_bit, i + 1)
        alu_out, load_pc, mem_dir = cpu.compute(instr, mem_in)

        assert cpu.a_register.value() == conversions.dec_to_bin_arr(n_bit, 100)
        assert cpu.d_register.value() == conversions.dec_to_bin_arr(n_bit, i + 1)
        assert load_pc == 0
        assert mem_dir == conversions.dec_to_bin_arr(n_bit, 16)

        instr = instructions[7]  # D = D-A
        mem_in = conversions.dec_to_bin_arr(n_bit, 0)
        alu_out, load_pc, mem_dir = cpu.compute(instr, mem_in)

        assert cpu.a_register.value() == conversions.dec_to_bin_arr(n_bit, 100)
        assert cpu.d_register.value() == cpu.alu.minus_x(conversions.dec_to_bin_arr(n_bit, (100 - (i + 1))), zero)
        assert load_pc == 0
        assert alu_out == cpu.alu.minus_x(conversions.dec_to_bin_arr(n_bit, (100 - (i + 1))), zero)
        assert mem_dir == conversions.dec_to_bin_arr(n_bit, 100)


        instr = instructions[8] # @END
        mem_in = conversions.dec_to_bin_arr(n_bit, 0)
        alu_out, load_pc, mem_dir = cpu.compute(instr, mem_in)

        assert cpu.a_register.value() == conversions.dec_to_bin_arr(n_bit, 18)
        assert cpu.d_register.value() == cpu.alu.minus_x(conversions.dec_to_bin_arr(n_bit, (100 - (i + 1))), zero)
        assert load_pc == 0
        assert mem_dir == conversions.dec_to_bin_arr(n_bit, 100)

        instr = instructions[9] # D;JGT
        mem_in = conversions.dec_to_bin_arr(n_bit, 0)
        alu_out, load_pc, mem_dir = cpu.compute(instr, mem_in)

        assert cpu.a_register.value() == conversions.dec_to_bin_arr(n_bit, 18)
        assert cpu.d_register.value() == cpu.alu.minus_x(conversions.dec_to_bin_arr(n_bit, (100 - (i + 1))), zero)
        assert load_pc == 0
        assert cpu.alu_out == cpu.alu.minus_x(conversions.dec_to_bin_arr(n_bit, (100 - (i + 1))), zero)
        assert mem_dir == conversions.dec_to_bin_arr(n_bit, 18)

        instr = instructions[10] # @i
        mem_in = conversions.dec_to_bin_arr(n_bit, 0)
        alu_out, load_pc, mem_dir = cpu.compute(instr, mem_in)

        assert cpu.a_register.value() == conversions.dec_to_bin_arr(n_bit, 16)
        assert cpu.d_register.value() == cpu.alu.minus_x(conversions.dec_to_bin_arr(n_bit, (100 - (i + 1))), zero)
        assert load_pc == 0
        assert mem_dir == conversions.dec_to_bin_arr(n_bit, 18)

        instr = instructions[11]  # D=M
        mem_in = conversions.dec_to_bin_arr(n_bit, i + 1)
        alu_out, load_pc, mem_dir = cpu.compute(instr, mem_in)

        assert cpu.a_register.value() == conversions.dec_to_bin_arr(n_bit, 16)
        assert cpu.d_register.value() == conversions.dec_to_bin_arr(n_bit, i + 1)
        assert load_pc == 0
        assert cpu.alu_out == conversions.dec_to_bin_arr(n_bit, i + 1)
        assert mem_dir == conversions.dec_to_bin_arr(n_bit, 16)

        instr = instructions[12]  # @sum
        mem_in = conversions.dec_to_bin_arr(n_bit, i + 1)
        alu_out, load_pc, mem_dir = cpu.compute(instr, mem_in)

        assert cpu.a_register.value() == conversions.dec_to_bin_arr(n_bit, 17)
        assert cpu.d_register.value() == conversions.dec_to_bin_arr(n_bit, i + 1)
        assert load_pc == 0
        assert mem_dir == conversions.dec_to_bin_arr(n_bit, 16)

        instr = instructions[13]  # M=D+M
        mem_in = conversions.dec_to_bin_arr(n_bit, 0)
        alu_out, load_pc, mem_dir = cpu.compute(instr, mem_in)

        assert cpu.a_register.value() == conversions.dec_to_bin_arr(n_bit, 17)
        assert cpu.d_register.value() == conversions.dec_to_bin_arr(n_bit, i+1)
        assert load_pc == 0
        assert cpu.alu_out == conversions.dec_to_bin_arr(n_bit, (sum_+i+1))
        assert mem_dir == conversions.dec_to_bin_arr(n_bit, 17)

        instr = instructions[14] # @i
        mem_in = conversions.dec_to_bin_arr(n_bit, (sum_+i+1))
        alu_out, load_pc, mem_dir = cpu.compute(instr, mem_in)

        assert cpu.a_register.value() == conversions.dec_to_bin_arr(n_bit, 16)
        assert cpu.d_register.value() == conversions.dec_to_bin_arr(n_bit, i+1)
        assert load_pc == 0
        assert mem_dir == conversions.dec_to_bin_arr(n_bit, 17)

        instr = instructions[15] # M=M+1
        mem_in = conversions.dec_to_bin_arr(n_bit, sum_+i+1)
        alu_out, load_pc, mem_dir = cpu.compute(instr, mem_in)

        assert cpu.a_register.value() == conversions.dec_to_bin_arr(n_bit, 16)
        assert cpu.d_register.value() == conversions.dec_to_bin_arr(n_bit, i+1)
        assert load_pc == 0
        assert mem_dir == conversions.dec_to_bin_arr(n_bit, 16)

        instr = instructions[16] # @LOOP
        mem_in = conversions.dec_to_bin_arr(n_bit, i + 2)
        alu_out, load_pc, mem_dir = cpu.compute(instr, mem_in)

        assert cpu.a_register.value() == conversions.dec_to_bin_arr(n_bit, 4)
        assert cpu.d_register.value() == conversions.dec_to_bin_arr(n_bit, i+1)
        assert load_pc == 0
        assert mem_dir == conversions.dec_to_bin_arr(n_bit, 16)

        instr = instructions[17] # 0;JMP
        mem_in = conversions.dec_to_bin_arr(n_bit, 0)
        alu_out, load_pc, mem_dir = cpu.compute(instr, mem_in)

        assert cpu.a_register.value() == conversions.dec_to_bin_arr(n_bit, 4)
        assert cpu.d_register.value() == conversions.dec_to_bin_arr(n_bit, i+1)
        assert load_pc == 1
        assert cpu.alu_out == conversions.dec_to_bin_arr(n_bit, 0)
        assert mem_dir == conversions.dec_to_bin_arr(n_bit, 4)

    instr = instructions[4]  # @i
    mem_in = conversions.dec_to_bin_arr(n_bit, 0)
    alu_out, load_pc, mem_dir = cpu.compute(instr, mem_in)

    assert cpu.a_register.value() == conversions.dec_to_bin_arr(n_bit, 16)
    assert cpu.d_register.value() == conversions.dec_to_bin_arr(n_bit, 100)
    assert load_pc == 0
    assert mem_dir == conversions.dec_to_bin_arr(n_bit, 4)

    instr = instructions[5]  # D = M
    mem_in = conversions.dec_to_bin_arr(n_bit, 101)
    alu_out, load_pc, mem_dir = cpu.compute(instr, mem_in)

    assert cpu.jump_decoder_out == 0
    assert cpu.a_register.value() == conversions.dec_to_bin_arr(n_bit, 16)
    assert cpu.d_register.value() == conversions.dec_to_bin_arr(n_bit, 101)
    assert load_pc == 0
    assert alu_out == conversions.dec_to_bin_arr(n_bit, 101)
    assert mem_dir == conversions.dec_to_bin_arr(n_bit, 16)


    instr = instructions[6]  # @100
    mem_in = conversions.dec_to_bin_arr(n_bit, 101)
    alu_out, load_pc, mem_dir = cpu.compute(instr, mem_in)

    assert cpu.a_register.value() == conversions.dec_to_bin_arr(n_bit, 100)
    assert cpu.d_register.value() == conversions.dec_to_bin_arr(n_bit, 101)
    assert load_pc == 0
    assert mem_dir == conversions.dec_to_bin_arr(n_bit, 16)

    instr = instructions[7]  # D = D-A
    mem_in = conversions.dec_to_bin_arr(n_bit, 0)
    alu_out, load_pc, mem_dir = cpu.compute(instr, mem_in)

    assert cpu.a_register.value() == conversions.dec_to_bin_arr(n_bit, 100)
    assert cpu.d_register.value() == conversions.dec_to_bin_arr(n_bit, 1)
    assert load_pc == 0
    assert alu_out == conversions.dec_to_bin_arr(n_bit, 1)
    assert mem_dir == conversions.dec_to_bin_arr(n_bit, 100)

    instr = instructions[8]  # @END
    mem_in = conversions.dec_to_bin_arr(n_bit, 0)
    alu_out, load_pc, mem_dir = cpu.compute(instr, mem_in)

    assert cpu.a_register.value() == conversions.dec_to_bin_arr(n_bit, 18)
    assert cpu.d_register.value() == conversions.dec_to_bin_arr(n_bit, 1)
    assert load_pc == 0
    assert mem_dir == conversions.dec_to_bin_arr(n_bit, 100)

    instr = instructions[9]  # D;JGT
    mem_in = conversions.dec_to_bin_arr(n_bit, 0)
    alu_out, load_pc, mem_dir = cpu.compute(instr, mem_in)

    assert cpu.a_register.value() == conversions.dec_to_bin_arr(n_bit, 18)
    assert cpu.d_register.value() == conversions.dec_to_bin_arr(n_bit, 1)
    assert load_pc == 1
    assert cpu.alu_out == conversions.dec_to_bin_arr(n_bit, 1)
    assert mem_dir == conversions.dec_to_bin_arr(n_bit, 18)

    instr = instructions[18]  # @END
    mem_in = conversions.dec_to_bin_arr(n_bit, 0)
    alu_out, load_pc, mem_dir = cpu.compute(instr, mem_in)

    assert cpu.a_register.value() == conversions.dec_to_bin_arr(n_bit, 18)
    assert cpu.d_register.value() == conversions.dec_to_bin_arr(n_bit, 1)
    assert load_pc == 0
    assert mem_dir == conversions.dec_to_bin_arr(n_bit, 18)


    instr = instructions[19]  # 0; JMP
    mem_in = conversions.dec_to_bin_arr(n_bit, 0)
    alu_out, load_pc, mem_dir = cpu.compute(instr, mem_in)

    assert cpu.a_register.value() == conversions.dec_to_bin_arr(n_bit, 18)
    assert cpu.d_register.value() == conversions.dec_to_bin_arr(n_bit, 1)
    assert load_pc == 1
    assert cpu.alu_out == conversions.dec_to_bin_arr(n_bit, 0)
    assert mem_dir == conversions.dec_to_bin_arr(n_bit, 18)
