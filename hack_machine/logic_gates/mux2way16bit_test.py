import pytest
from hack_machine.logic_gates.mux2way16bit import Mux2Way16Bit
from hack_machine.utils import conversions
from random import randrange

n_iterations = 400
n_bit = 16
random_ceil = conversions.bin_to_dec('1' * 16)

mux2Way16Bit = Mux2Way16Bit()


def test_mux2way16bit():
    for i in range(400):
        sel = i % 2

        a_dec = randrange(random_ceil)
        a_bin = conversions.dec_to_bin_arr(n_bit, a_dec)

        b_dec = randrange(random_ceil)
        b_bin = conversions.dec_to_bin_arr(n_bit, b_dec)

        result = mux2Way16Bit.compute(sel, a_bin, b_bin)

        if sel == 0:
            expected_out = a_bin
            assert result == expected_out, 'Error, the input sel{}, a{}, b{} should output: {} but instead got: {}'.format(sel,
                                                                                                                         a_bin,
                                                                                                                         b_bin,
                                                                                                                         expected_out,
                                                                                                                         result)
        else:
            expected_out = b_bin
            assert result == expected_out, 'Error, the input sel{}, a{}, b{} should output: {} but instead got: {}'.format(sel,
                                                                                                                         a_bin,
                                                                                                                         b_bin,
                                                                                                                         expected_out,
                                                                                                                         result)