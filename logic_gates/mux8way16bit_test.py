import pytest
import sys
import os

sys.path.append(os.environ['ROOT_FOLDER'] + '/logic_gates')
from mux8way16bit import Mux8Way16Bit

sys.path.append(os.environ['ROOT_FOLDER'] + '/utils')
import conversions

from random import randrange

n_iterations = 400
n_bit = 16
random_ceil = conversions.bin_to_dec('1' * 16)

mux8Way16Bit = Mux8Way16Bit()

def test_mux8way16bit():
    for i in range(n_iterations):
        sel = [randrange(2), randrange(2), randrange(2)]

        a_dec = randrange(random_ceil)
        a_bin = conversions.dec_to_bin_arr(n_bit, a_dec)

        b_dec = randrange(random_ceil)
        b_bin = conversions.dec_to_bin_arr(n_bit, b_dec)

        c_dec = randrange(random_ceil)
        c_bin = conversions.dec_to_bin_arr(n_bit, c_dec)

        d_dec = randrange(random_ceil)
        d_bin = conversions.dec_to_bin_arr(n_bit, d_dec)

        e_dec = randrange(random_ceil)
        e_bin = conversions.dec_to_bin_arr(n_bit, e_dec)

        f_dec = randrange(random_ceil)
        f_bin = conversions.dec_to_bin_arr(n_bit, f_dec)

        g_dec = randrange(random_ceil)
        g_bin = conversions.dec_to_bin_arr(n_bit, g_dec)

        h_dec = randrange(random_ceil)
        h_bin = conversions.dec_to_bin_arr(n_bit, h_dec)

        result = mux8Way16Bit.compute(sel, a_bin, b_bin, c_bin, d_bin, e_bin, f_bin, g_bin, h_bin)

        if sel == [0, 0, 0]:
            expected_out = a_bin
            assert expected_out == result, 'Error, the input sel: {}, a: {}, b: {}, c: {}, d: {} should output: {} but instead got: {}'.format(sel,
                                                                                                                                   a_dec,
                                                                                                                                   b_dec,
                                                                                                                                   c_dec,
                                                                                                                                   d_dec,
                                                                                                                                   expected_out,
                                                                                                                                   result)
        elif sel == [0, 0, 1]:
            expected_out = b_bin
            assert expected_out == result, 'Error, the input sel: {}, a: {}, b: {}, c: {}, d: {} should output: {} but instead got: {}'.format(
                sel,
                a_dec,
                b_dec,
                c_dec,
                d_dec,
                expected_out,
                result)

        elif sel == [0, 1, 0]:
            expected_out = c_bin
            assert expected_out == result, 'Error, the input sel: {}, a: {}, b: {}, c: {}, d: {} should output: {} but instead got: {}'.format(
                sel,
                a_dec,
                b_dec,
                c_dec,
                d_dec,
                expected_out,
                result)

        elif sel == [0, 1, 1]:
            expected_out = d_bin
            assert expected_out == result, 'Error, the input sel: {}, a: {}, b: {}, c: {}, d: {} should output: {} but instead got: {}'.format(
                sel,
                a_dec,
                b_dec,
                c_dec,
                d_dec,
                expected_out,
                result)

        elif sel == [1, 0, 0]:
            expected_out = e_bin
            assert expected_out == result, 'Error, the input sel: {}, a: {}, b: {}, c: {}, d: {} should output: {} but instead got: {}'.format(
                sel,
                a_dec,
                b_dec,
                c_dec,
                d_dec,
                expected_out,
                result)

        elif sel == [1, 0, 1]:
            expected_out = f_bin
            assert expected_out == result, 'Error, the input sel: {}, a: {}, b: {}, c: {}, d: {} should output: {} but instead got: {}'.format(
                sel,
                a_dec,
                b_dec,
                c_dec,
                d_dec,
                expected_out,
                result)

        elif sel == [1, 1, 0]:
            expected_out = g_bin
            assert expected_out == result, 'Error, the input sel: {}, a: {}, b: {}, c: {}, d: {} should output: {} but instead got: {}'.format(
                sel,
                a_dec,
                b_dec,
                c_dec,
                d_dec,
                expected_out,
                result)

        elif sel == [1, 1, 1]:
            expected_out = h_bin
            assert expected_out == result, 'Error, the input sel: {}, a: {}, b: {}, c: {}, d: {} should output: {} but instead got: {}'.format(
                sel,
                a_dec,
                b_dec,
                c_dec,
                d_dec,
                expected_out,
                result)