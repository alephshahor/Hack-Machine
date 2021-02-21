import pytest
from hack_machine.logic_gates.dmux4way16bit import DMux4Way16Bit
from hack_machine.utils import conversions
from random import randrange

n_iterations = 400
n_bit = 16
random_ceil = conversions.bin_to_dec('1' * 16)
zero = conversions.dec_to_bin_arr(n_bit, 0)

dMux4Way16Bit = DMux4Way16Bit()

def expected_result_to_dec(expected_result):
    return [conversions.bin_arr_to_dec(expected_result[0]),
            conversions.bin_arr_to_dec(expected_result[1]),
            conversions.bin_arr_to_dec(expected_result[2]),
            conversions.bin_arr_to_dec(expected_result[3])]

def test_demux4way16bit():
    for i in range(n_iterations):
        selector_input = [randrange(2), randrange(2)]

        input_dec = randrange(random_ceil)
        input_bin = conversions.dec_to_bin_arr(n_bit, input_dec)

        result = dMux4Way16Bit.compute(selector_input, input_bin)
        result_dec = [conversions.bin_arr_to_dec(result[0]), conversions.bin_arr_to_dec(result[1]),
                      conversions.bin_arr_to_dec(result[2]), conversions.bin_arr_to_dec(result[3])]

        if selector_input == [0, 0]:
            expected_result = [input_bin, zero, zero, zero]
            expected_result_dec = expected_result_to_dec(expected_result)
            assert result == expected_result, 'Error, sel{}, in[{}] should output: {} but got: {}'.format(selector_input,
                                                                                                        input_dec,
                                                                                                        expected_result_dec,
                                                                                                        result_dec)
        elif selector_input == [0, 1]:
            expected_result = [zero, input_bin, zero, zero]
            expected_result_dec = expected_result_to_dec(expected_result)
            assert result == expected_result, 'Error, sel{}, in[{}] should output: {} but got: {}'.format(selector_input,
                                                                                                        input_dec,
                                                                                                        expected_result_dec,
                                                                                                        result_dec)
        elif selector_input == [1, 0]:
            expected_result = [zero, zero, input_bin, zero]
            expected_result_dec = expected_result_to_dec(expected_result)
            assert result == expected_result, 'Error, sel{}, in[{}] should output: {} but got: {}'.format(selector_input,
                                                                                                        input_dec,
                                                                                                        expected_result_dec,
                                                                                                        result_dec)
        elif selector_input == [1, 1]:
            expected_result = [zero, zero, zero, input_bin]
            expected_result_dec = expected_result_to_dec(expected_result)
            assert result == expected_result, 'Error, sel{}, in[{}] should output: {} but got: {}'.format(selector_input,
                                                                                                        input_dec,
                                                                                                        expected_result_dec,
                                                                                                        result_dec)