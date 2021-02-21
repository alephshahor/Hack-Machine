import pytest
from hack_machine.logic_gates.dmux8way16bit import DMux8Way16Bit
from hack_machine.utils import conversions
from random import randrange

'''
test_input =  [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1], [0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1], [0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1], [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0]]
test_sel    = [[0,0,0],[0,0,1],[0,1,0],[0,1,1],[1,0,0],[1,0,1],[1,1,0],[1,1,1]]
test_output = [[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]],
               [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]],
               [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]],
               [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]],
               [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]],
               [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]],
               [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]],
               [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0]]]
'''

n_iterations = 100
n_bit = 16
random_ceil = conversions.bin_to_dec('1' * 16)
zero = conversions.dec_to_bin_arr(n_bit, 0)

dMux8Way16Bit = DMux8Way16Bit()

def expected_result_to_dec(expected_result):
    return [conversions.bin_arr_to_dec(expected_result[0]),
            conversions.bin_arr_to_dec(expected_result[1]),
            conversions.bin_arr_to_dec(expected_result[2]),
            conversions.bin_arr_to_dec(expected_result[3]),
            conversions.bin_arr_to_dec(expected_result[4]),
            conversions.bin_arr_to_dec(expected_result[5]),
            conversions.bin_arr_to_dec(expected_result[6]),
            conversions.bin_arr_to_dec(expected_result[7]),
            ]

def test_demux8way16bit():
    for i in range(n_iterations):
        selector_input = [randrange(2), randrange(2), randrange(2)]

        input_dec = randrange(random_ceil)
        input_bin = conversions.dec_to_bin_arr(n_bit, input_dec)

        result = dMux8Way16Bit.compute(selector_input, input_bin)
        result_dec = [conversions.bin_arr_to_dec(result[0]), conversions.bin_arr_to_dec(result[1]),
                      conversions.bin_arr_to_dec(result[2]), conversions.bin_arr_to_dec(result[3]),
                      conversions.bin_arr_to_dec(result[4]), conversions.bin_arr_to_dec(result[5]),
                      conversions.bin_arr_to_dec(result[6]), conversions.bin_arr_to_dec(result[7])]

        if selector_input == [0, 0, 0]:
            expected_result = [input_bin, zero, zero, zero, zero, zero, zero, zero]
            expected_result_dec = expected_result_to_dec(expected_result)
            assert result == expected_result, 'Error, sel{}, in[{}] should output: {} but got: {}'.format(selector_input,
                                                                                                        input_dec,
                                                                                                        expected_result_dec,
                                                                                                        result_dec)
        elif selector_input == [0, 0, 1]:
            expected_result = [zero, input_bin, zero, zero, zero, zero, zero, zero]
            expected_result_dec = expected_result_to_dec(expected_result)
            assert result == expected_result, 'Error, sel{}, in[{}] should output: {} but got: {}'.format(selector_input,
                                                                                                        input_dec,
                                                                                                        expected_result_dec,
                                                                                                        result_dec)
        elif selector_input == [0, 1, 0]:
            expected_result = [zero, zero, input_bin, zero, zero, zero, zero, zero]
            expected_result_dec = expected_result_to_dec(expected_result)
            assert result == expected_result, 'Error, sel{}, in[{}] should output: {} but got: {}'.format(selector_input,
                                                                                                        input_dec,
                                                                                                        expected_result_dec,
                                                                                                        result_dec)
        elif selector_input == [0, 1, 1]:
            expected_result = [zero, zero, zero, input_bin, zero, zero, zero, zero]
            expected_result_dec = expected_result_to_dec(expected_result)
            assert result == expected_result, 'Error, sel{}, in[{}] should output: {} but got: {}'.format(selector_input,
                                                                                                        input_dec,
                                                                                                        expected_result_dec,
                                                                                                        result_dec)
        elif selector_input == [1, 0, 0]:
            expected_result = [zero, zero, zero, zero, input_bin, zero, zero, zero]
            expected_result_dec = expected_result_to_dec(expected_result)
            assert result == expected_result, 'Error, sel{}, in[{}] should output: {} but got: {}'.format(selector_input,
                                                                                                        input_dec,
                                                                                                        expected_result_dec,
                                                                                                        result_dec)
        elif selector_input == [1, 0, 1]:
            expected_result = [zero, zero, zero, zero, zero, input_bin, zero, zero]
            expected_result_dec = expected_result_to_dec(expected_result)
            assert result == expected_result, 'Error, sel{}, in[{}] should output: {} but got: {}'.format(selector_input, input_dec,
                                                                                                        expected_result_dec,
                                                                                                        result_dec)
        elif selector_input == [1, 1, 0]:
            expected_result = [zero, zero, zero, zero, zero, zero, input_bin, zero]
            expected_result_dec = expected_result_to_dec(expected_result)
            assert result == expected_result, 'Error, sel{}, in[{}] should output: {} but got: {}'.format(selector_input,
                                                                                                        input_dec,
                                                                                                        expected_result_dec,
                                                                                                        result_dec)
        elif selector_input == [1, 1, 1]:
            expected_result = [zero, zero, zero, zero, zero, zero, zero, input_bin]
            expected_result_dec = expected_result_to_dec(expected_result)
            assert result == expected_result, 'Error, sel{}, in[{}] should output: {} but got: {}'.format(selector_input,
                                                                                                        input_dec,
                                                                                                        expected_result_dec,
                                                                                                        result_dec)