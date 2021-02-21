import sys
from hack_machine.logic_gates.dmux2way16bit import DMux2Way16Bit
from hack_machine.utils import conversions
from random import randrange

n_iterations = 100
n_bit = 16
random_ceil = conversions.bin_to_dec('1' * 16)

dMux2Way16Bit = DMux2Way16Bit()
zero = conversions.dec_to_bin_arr(n_bit, 0)


def test_dmux2way16bit():
    for i in range(n_iterations):
        selector_input = i % 2

        input_dec = randrange(random_ceil)
        input_bin = conversions.dec_to_bin_arr(n_bit, input_dec)

        result = dMux2Way16Bit.compute(selector_input, input_bin)

        if selector_input:
            assert result == [zero, input_bin], 'Error, sel[{}], in{} should output: {} but got: {}'.format(selector_input,
                                                                                                            input_dec,
                                                                                                            [0, input_dec],
                                                                                                            [conversions.bin_arr_to_dec(result[0]), conversions.bin_arr_to_dec(result[1])])
        else:
            assert result == [input_bin, zero], 'Error, sel[{}], in{} should output: {} but got: {}'.format(selector_input,
                                                                                                            input_bin,
                                                                                                            [zero, input_bin],
                                                                                                            [conversions.bin_arr_to_dec(result[0]),conversions.bin_arr_to_dec(result[1])])