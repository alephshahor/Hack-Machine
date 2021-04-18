import sys
import os

sys.path.append(os.environ['ROOT_FOLDER'])
from emulator import Emulator

sys.path.append(os.environ['ROOT_FOLDER'] + '/utils')
import conversions

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

emulator = Emulator()
zero = [0] * 16
one = zero[:15] + [1]
n_bit = 16

def test_emulator():

    n_iterations = 3

    emulator.load_instructions_mock(instructions)

    for i, instr in enumerate(instructions):
        assert emulator.instruction_memory.mem[i] == instr

    # @i
    emulator.run(1)

    assert emulator.cpu.a_register.value() == conversions.dec_to_bin_arr(n_bit, 16)
    assert emulator.cpu.d_register.value() == zero
    assert emulator.data_memory.mem[conversions.bin_arr_to_dec(instructions[0])] == zero

    # M=1
    emulator.run(1)

    assert emulator.cpu.a_register.value() == conversions.dec_to_bin_arr(n_bit, 16)
    assert emulator.cpu.d_register.value() == zero
    assert emulator.data_memory.mem[conversions.bin_arr_to_dec(instructions[0])] == zero

    # @sum
    emulator.run(1)

    assert emulator.cpu.a_register.value() == conversions.dec_to_bin_arr(n_bit, 17)
    assert emulator.cpu.d_register.value() == zero
    assert emulator.data_memory.mem[conversions.bin_arr_to_dec(instructions[0])] == one
    assert emulator.data_memory.mem[conversions.bin_arr_to_dec(instructions[2])] == zero

    # M=0
    emulator.run(1)

    assert emulator.cpu.a_register.value() == conversions.dec_to_bin_arr(n_bit, 17)
    assert emulator.cpu.d_register.value() == zero
    assert emulator.data_memory.mem[conversions.bin_arr_to_dec(instructions[0])] == one
    assert emulator.data_memory.mem[conversions.bin_arr_to_dec(instructions[2])] == zero

    sum_value = conversions.dec_to_bin_arr(n_bit, 0)

    for i in range(100):

        # @i
        emulator.run(1)
        assert emulator.cpu.a_register.value() == conversions.dec_to_bin_arr(n_bit, 16)
        assert emulator.cpu.d_register.value() == conversions.dec_to_bin_arr(n_bit, i)
        assert emulator.data_memory.mem[conversions.bin_arr_to_dec(instructions[0])] == conversions.dec_to_bin_arr(n_bit, i + 1)
        assert emulator.data_memory.mem[conversions.bin_arr_to_dec(instructions[2])] == sum_value

        # D=M
        emulator.run(1)
        assert emulator.cpu.a_register.value() == conversions.dec_to_bin_arr(n_bit, 16)
        assert emulator.cpu.d_register.value() == conversions.dec_to_bin_arr(n_bit, i + 1)
        assert emulator.data_memory.mem[conversions.bin_arr_to_dec(instructions[0])] == conversions.dec_to_bin_arr(n_bit, i + 1)
        assert emulator.data_memory.mem[conversions.bin_arr_to_dec(instructions[2])] == sum_value

        # @100
        emulator.run(1)
        assert emulator.cpu.a_register.value() == conversions.dec_to_bin_arr(n_bit, 100)
        assert emulator.cpu.d_register.value() == conversions.dec_to_bin_arr(n_bit, i + 1)
        assert emulator.data_memory.mem[conversions.bin_arr_to_dec(instructions[0])] == conversions.dec_to_bin_arr(n_bit, i + 1)
        assert emulator.data_memory.mem[conversions.bin_arr_to_dec(instructions[2])] == sum_value

        # D = D-A
        emulator.run(1)
        assert emulator.cpu.a_register.value() == conversions.dec_to_bin_arr(n_bit, 100)
        assert emulator.cpu.d_register.value() == emulator.cpu.alu.minus_x(conversions.dec_to_bin_arr(n_bit, (100 - (i + 1))), zero)
        assert emulator.data_memory.mem[conversions.bin_arr_to_dec(instructions[0])] == conversions.dec_to_bin_arr(n_bit, i + 1)
        assert emulator.data_memory.mem[conversions.bin_arr_to_dec(instructions[2])] == sum_value

        # @END
        emulator.run(1)
        assert emulator.cpu.a_register.value() == conversions.dec_to_bin_arr(n_bit, 18)
        assert emulator.cpu.d_register.value() == emulator.cpu.alu.minus_x(conversions.dec_to_bin_arr(n_bit, (100 - (i + 1))), zero)
        assert emulator.data_memory.mem[conversions.bin_arr_to_dec(instructions[0])] == conversions.dec_to_bin_arr(n_bit, i + 1)
        assert emulator.data_memory.mem[conversions.bin_arr_to_dec(instructions[2])] == sum_value

        # D;JGT
        emulator.run(1)
        assert emulator.cpu.a_register.value() == conversions.dec_to_bin_arr(n_bit, 18)
        assert emulator.cpu.d_register.value() == emulator.cpu.alu.minus_x(conversions.dec_to_bin_arr(n_bit, (100 - (i + 1))), zero)
        assert emulator.data_memory.mem[conversions.bin_arr_to_dec(instructions[0])] == conversions.dec_to_bin_arr(n_bit, i + 1)
        assert emulator.data_memory.mem[conversions.bin_arr_to_dec(instructions[2])] == sum_value

        # @i
        emulator.run(1)
        assert emulator.cpu.a_register.value() == conversions.dec_to_bin_arr(n_bit, 16)
        assert emulator.cpu.d_register.value() == emulator.cpu.alu.minus_x(conversions.dec_to_bin_arr(n_bit, (100 - (i + 1))), zero)
        assert emulator.data_memory.mem[conversions.bin_arr_to_dec(instructions[0])] == conversions.dec_to_bin_arr(n_bit, i + 1)
        assert emulator.data_memory.mem[conversions.bin_arr_to_dec(instructions[2])] == sum_value

        # D=M
        emulator.run(1)
        assert emulator.cpu.a_register.value() == conversions.dec_to_bin_arr(n_bit, 16)
        assert emulator.cpu.d_register.value() == conversions.dec_to_bin_arr(n_bit, i + 1)
        assert emulator.data_memory.mem[conversions.bin_arr_to_dec(instructions[0])] == conversions.dec_to_bin_arr(n_bit, i + 1)
        assert emulator.data_memory.mem[conversions.bin_arr_to_dec(instructions[2])] == sum_value

        # @sum
        emulator.run(1)
        assert emulator.cpu.a_register.value() == conversions.dec_to_bin_arr(n_bit, 17)
        assert emulator.cpu.d_register.value() == conversions.dec_to_bin_arr(n_bit, i + 1)
        assert emulator.data_memory.mem[conversions.bin_arr_to_dec(instructions[0])] == conversions.dec_to_bin_arr(n_bit, i + 1)
        assert emulator.data_memory.mem[conversions.bin_arr_to_dec(instructions[2])] == sum_value

        # M=D+M
        sum_value_temp = sum_value
        sum_value = emulator.cpu.alu.x_plus_y(emulator.cpu.d_register.value(), emulator.data_memory.mem[conversions.bin_arr_to_dec(instructions[2])])

        emulator.run(1)
        assert emulator.cpu.a_register.value() == conversions.dec_to_bin_arr(n_bit, 17)
        assert emulator.cpu.d_register.value() == conversions.dec_to_bin_arr(n_bit, i + 1)
        assert emulator.data_memory.mem[conversions.bin_arr_to_dec(instructions[0])] == conversions.dec_to_bin_arr(n_bit, i + 1)
        assert emulator.data_memory.mem[conversions.bin_arr_to_dec(instructions[2])] == sum_value_temp

        # @i
        emulator.run(1)
        assert emulator.cpu.a_register.value() == conversions.dec_to_bin_arr(n_bit, 16)
        assert emulator.cpu.d_register.value() == conversions.dec_to_bin_arr(n_bit, i + 1)
        assert emulator.data_memory.mem[conversions.bin_arr_to_dec(instructions[0])] == conversions.dec_to_bin_arr(n_bit, i + 1)
        assert emulator.data_memory.mem[conversions.bin_arr_to_dec(instructions[2])] == sum_value

        # M=M+1
        emulator.run(1)
        assert emulator.cpu.a_register.value() == conversions.dec_to_bin_arr(n_bit, 16)
        assert emulator.cpu.d_register.value() == conversions.dec_to_bin_arr(n_bit, i + 1)
        assert emulator.data_memory.mem[conversions.bin_arr_to_dec(instructions[0])] == conversions.dec_to_bin_arr(n_bit, i + 1)
        assert emulator.data_memory.mem[conversions.bin_arr_to_dec(instructions[2])] == sum_value

        # @LOOP
        emulator.run(1)
        assert emulator.cpu.a_register.value() == conversions.dec_to_bin_arr(n_bit, 4)
        assert emulator.cpu.d_register.value() == conversions.dec_to_bin_arr(n_bit, i + 1)
        assert emulator.data_memory.mem[conversions.bin_arr_to_dec(instructions[0])] == conversions.dec_to_bin_arr(n_bit, i + 2)
        assert emulator.data_memory.mem[conversions.bin_arr_to_dec(instructions[2])] == sum_value

        # 0;JMP
        emulator.run(1)
        assert emulator.cpu.a_register.value() == conversions.dec_to_bin_arr(n_bit, 4)
        assert emulator.cpu.d_register.value() == conversions.dec_to_bin_arr(n_bit, i + 1)
        assert emulator.data_memory.mem[conversions.bin_arr_to_dec(instructions[0])] == conversions.dec_to_bin_arr(n_bit, i + 2)
        assert emulator.data_memory.mem[conversions.bin_arr_to_dec(instructions[2])] == sum_value

    # @i
    emulator.run(1)
    assert emulator.cpu.a_register.value() == conversions.dec_to_bin_arr(n_bit, 16)
    assert emulator.cpu.d_register.value() == conversions.dec_to_bin_arr(n_bit, 100)
    assert emulator.data_memory.mem[conversions.bin_arr_to_dec(instructions[0])] == conversions.dec_to_bin_arr(n_bit, 101)
    assert emulator.data_memory.mem[conversions.bin_arr_to_dec(instructions[2])] == sum_value

    # D=M
    emulator.run(1)
    assert emulator.cpu.a_register.value() == conversions.dec_to_bin_arr(n_bit, 16)
    assert emulator.cpu.d_register.value() == conversions.dec_to_bin_arr(n_bit, 101)
    assert emulator.data_memory.mem[conversions.bin_arr_to_dec(instructions[0])] == conversions.dec_to_bin_arr(n_bit,
                                                                                                               101)
    assert emulator.data_memory.mem[conversions.bin_arr_to_dec(instructions[2])] == sum_value

    # @100
    emulator.run(1)
    assert emulator.cpu.a_register.value() == conversions.dec_to_bin_arr(n_bit, 100)
    assert emulator.cpu.d_register.value() == conversions.dec_to_bin_arr(n_bit, 101)
    assert emulator.data_memory.mem[conversions.bin_arr_to_dec(instructions[0])] == conversions.dec_to_bin_arr(n_bit,
                                                                                                               101)
    assert emulator.data_memory.mem[conversions.bin_arr_to_dec(instructions[2])] == sum_value

    # D=D-A
    emulator.run(1)
    assert emulator.cpu.a_register.value() == conversions.dec_to_bin_arr(n_bit, 100)
    assert emulator.cpu.d_register.value() == conversions.dec_to_bin_arr(n_bit, 1)
    assert emulator.data_memory.mem[conversions.bin_arr_to_dec(instructions[0])] == conversions.dec_to_bin_arr(n_bit,
                                                                                                               101)
    assert emulator.data_memory.mem[conversions.bin_arr_to_dec(instructions[2])] == sum_value

    # @END
    emulator.run(1)
    assert emulator.cpu.a_register.value() == conversions.dec_to_bin_arr(n_bit, 18)
    assert emulator.cpu.d_register.value() == conversions.dec_to_bin_arr(n_bit, 1)
    assert emulator.data_memory.mem[conversions.bin_arr_to_dec(instructions[0])] == conversions.dec_to_bin_arr(n_bit,
                                                                                                               101)
    assert emulator.data_memory.mem[conversions.bin_arr_to_dec(instructions[2])] == sum_value

    # D;JGT
    emulator.run(1)
    assert emulator.cpu.a_register.value() == conversions.dec_to_bin_arr(n_bit, 18)
    assert emulator.cpu.d_register.value() == conversions.dec_to_bin_arr(n_bit, 1)
    assert emulator.data_memory.mem[conversions.bin_arr_to_dec(instructions[0])] == conversions.dec_to_bin_arr(n_bit,
                                                                                                               101)
    assert emulator.data_memory.mem[conversions.bin_arr_to_dec(instructions[2])] == sum_value

    # @END
    emulator.run(1)
    assert emulator.cpu.a_register.value() == conversions.dec_to_bin_arr(n_bit, 18)
    assert emulator.cpu.d_register.value() == conversions.dec_to_bin_arr(n_bit, 1)
    assert emulator.data_memory.mem[conversions.bin_arr_to_dec(instructions[0])] == conversions.dec_to_bin_arr(n_bit,
                                                                                                               101)
    assert emulator.data_memory.mem[conversions.bin_arr_to_dec(instructions[2])] == sum_value

    # 0; JMP
    emulator.run(1)
    assert emulator.cpu.a_register.value() == conversions.dec_to_bin_arr(n_bit, 18)
    assert emulator.cpu.d_register.value() == conversions.dec_to_bin_arr(n_bit, 1)
    assert emulator.data_memory.mem[conversions.bin_arr_to_dec(instructions[0])] == conversions.dec_to_bin_arr(n_bit,
                                                                                                               101)
    assert emulator.data_memory.mem[conversions.bin_arr_to_dec(instructions[2])] == sum_value