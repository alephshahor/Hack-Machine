import pytest
from hack_machine.logic_gates.mux4way16bit import Mux4Way16Bit
from hack_machine.utils import conversions
from random import randrange

n_iterations = 400
n_bit = 16
random_ceil = conversions.bin_to_dec('1' * 16)

mux4Way16Bit = Mux4Way16Bit()


def test_mux4way16bit():
    for i in range(n_iterations):
        sel = [randrange(2), randrange(2)]

        a_dec = randrange(random_ceil)
        a_bin = conversions.dec_to_bin_arr(n_bit, a_dec)

        b_dec = randrange(random_ceil)
        b_bin = conversions.dec_to_bin_arr(n_bit, b_dec)

        c_dec = randrange(random_ceil)
        c_bin = conversions.dec_to_bin_arr(n_bit, c_dec)

        d_dec = randrange(random_ceil)
        d_bin = conversions.dec_to_bin_arr(n_bit, d_dec)

        result = mux4Way16Bit.compute(sel, a_bin, b_bin, c_bin, d_bin)

        if sel == [0, 0]:
            expected_out = a_bin
            assert expected_out == result, 'Error, the input sel: {}, a: {}, b: {}, c: {}, d: {} should output: {} but instead got: {}'.format(sel,
                                                                                                                                   a_dec,
                                                                                                                                   b_dec,
                                                                                                                                   c_dec,
                                                                                                                                   d_dec,
                                                                                                                                   expected_out,
                                                                                                                                   result)
        elif sel == [0, 1]:
            expected_out = b_bin
            assert expected_out == result, 'Error, the input sel: {}, a: {}, b: {}, c: {}, d: {} should output: {} but instead got: {}'.format(
                sel,
                a_dec,
                b_dec,
                c_dec,
                d_dec,
                expected_out,
                result)

        elif sel == [1, 0]:
            expected_out = c_bin
            assert expected_out == result, 'Error, the input sel: {}, a: {}, b: {}, c: {}, d: {} should output: {} but instead got: {}'.format(
                sel,
                a_dec,
                b_dec,
                c_dec,
                d_dec,
                expected_out,
                result)

        elif sel == [1, 1]:
            expected_out = d_bin
            assert expected_out == result, 'Error, the input sel: {}, a: {}, b: {}, c: {}, d: {} should output: {} but instead got: {}'.format(
                sel,
                a_dec,
                b_dec,
                c_dec,
                d_dec,
                expected_out,
                result)