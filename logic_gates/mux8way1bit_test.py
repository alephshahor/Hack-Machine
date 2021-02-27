import sys
import os

sys.path.append(os.environ['ROOT_FOLDER'] + '/logic_gates')
from mux8way1bit import Mux8Way1Bit

sys.path.append(os.environ['ROOT_FOLDER'] + '/utils')
import conversions

from random import randrange

'''
test_a_input = [1, 0, 0, 0, 0, 0, 0, 0]
test_b_input = [0, 1, 0, 0, 0, 0, 0, 0]
test_c_input = [0, 0, 1, 0, 0, 0, 0, 0]
test_d_input = [0, 0, 0, 1, 0, 0, 0, 0]
test_e_input = [0, 0, 0, 0, 1, 0, 0, 0]
test_f_input = [0, 0, 0, 0, 0, 1, 0, 0]
test_g_input = [0, 0, 0, 0, 0, 0, 1, 0]
test_h_input = [0, 0, 0, 0, 0, 0, 0, 1]

test_sel_input = [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]]

test_output = [1, 1, 1, 1, 1, 1, 1, 1]
'''

n_iterations = 400
n_bit = 16
random_ceil = conversions.bin_to_dec('1' * 16)

mux8Way1Bit = Mux8Way1Bit()

def test_mux8way1bit():
    for i in range(n_iterations):

        sel = [randrange(2), randrange(2), randrange(2)]
        sel_dec = conversions.bin_arr_to_dec(sel)

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

        result = mux8Way1Bit.compute(sel, a_bin, b_bin, c_bin, d_bin, e_bin, f_bin, g_bin, h_bin)
        result_dec = conversions.bin_arr_to_dec(result)

        if sel == [0, 0, 0]:
            expected_out = a_bin
            expected_out_dec = conversions.bin_arr_to_dec(expected_out)
            assert result == expected_out, 'Error, the input sel: {}, a: {}, b: {}, c: {}, d: {}, e: {}, f: {}, '\
                                           'g: {}, h: {} should output: {} but instead got: {}'.format(sel_dec,
                                                                                                       a_dec,
                                                                                                       b_dec,
                                                                                                       c_dec,
                                                                                                       d_dec,
                                                                                                       e_dec,
                                                                                                       f_dec,
                                                                                                       g_dec,
                                                                                                       h_dec,
                                                                                                       expected_out_dec,
                                                                                                       result_dec)
        if sel == [0, 0, 1]:
            expected_out = b_bin
            expected_out_dec = conversions.bin_arr_to_dec(expected_out)
            assert result == expected_out, 'Error, the input sel: {}, a: {}, b: {}, c: {}, d: {}, e: {}, f: {}, ' \
                                           'g: {}, h: {} should output: {} but instead got: {}'.format(sel_dec,
                                                                                                       a_dec,
                                                                                                       b_dec,
                                                                                                       c_dec,
                                                                                                       d_dec,
                                                                                                       e_dec,
                                                                                                       f_dec,
                                                                                                       g_dec,
                                                                                                       h_dec,
                                                                                                       expected_out_dec,
                                                                                                       result_dec)
        if sel == [0, 1, 0]:
            expected_out = c_bin
            expected_out_dec = conversions.bin_arr_to_dec(expected_out)
            assert result == expected_out, 'Error, the input sel: {}, a: {}, b: {}, c: {}, d: {}, e: {}, f: {}, ' \
                                           'g: {}, h: {} should output: {} but instead got: {}'.format(sel_dec,
                                                                                                       a_dec,
                                                                                                       b_dec,
                                                                                                       c_dec,
                                                                                                       d_dec,
                                                                                                       e_dec,
                                                                                                       f_dec,
                                                                                                       g_dec,
                                                                                                       h_dec,
                                                                                                       expected_out_dec,
                                                                                                       result_dec)
        if sel == [0, 1, 1]:
            expected_out = d_bin
            expected_out_dec = conversions.bin_arr_to_dec(expected_out)
            assert result == expected_out, 'Error, the input sel: {}, a: {}, b: {}, c: {}, d: {}, e: {}, f: {}, ' \
                                           'g: {}, h: {} should output: {} but instead got: {}'.format(sel_dec,
                                                                                                       a_dec,
                                                                                                       b_dec,
                                                                                                       c_dec,
                                                                                                       d_dec,
                                                                                                       e_dec,
                                                                                                       f_dec,
                                                                                                       g_dec,
                                                                                                       h_dec,
                                                                                                       expected_out_dec,
                                                                                                       result_dec)
        if sel == [1, 0, 0]:
            expected_out = e_bin
            expected_out_dec = conversions.bin_arr_to_dec(expected_out)
            assert result == expected_out, 'Error, the input sel: {}, a: {}, b: {}, c: {}, d: {}, e: {}, f: {}, ' \
                                           'g: {}, h: {} should output: {} but instead got: {}'.format(sel_dec,
                                                                                                       a_dec,
                                                                                                       b_dec,
                                                                                                       c_dec,
                                                                                                       d_dec,
                                                                                                       e_dec,
                                                                                                       f_dec,
                                                                                                       g_dec,
                                                                                                       h_dec,
                                                                                                       expected_out_dec,
                                                                                                       result_dec)
        if sel == [1, 0, 1]:
            expected_out = f_bin
            expected_out_dec = conversions.bin_arr_to_dec(expected_out)
            assert result == expected_out, 'Error, the input sel: {}, a: {}, b: {}, c: {}, d: {}, e: {}, f: {}, ' \
                                           'g: {}, h: {} should output: {} but instead got: {}'.format(sel_dec,
                                                                                                       a_dec,
                                                                                                       b_dec,
                                                                                                       c_dec,
                                                                                                       d_dec,
                                                                                                       e_dec,
                                                                                                       f_dec,
                                                                                                       g_dec,
                                                                                                       h_dec,
                                                                                                       expected_out_dec,
                                                                                                       result_dec)
        if sel == [1, 1, 0]:
            expected_out = g_bin
            expected_out_dec = conversions.bin_arr_to_dec(expected_out)
            assert result == expected_out, 'Error, the input sel: {}, a: {}, b: {}, c: {}, d: {}, e: {}, f: {}, ' \
                                           'g: {}, h: {} should output: {} but instead got: {}'.format(sel_dec,
                                                                                                       a_dec,
                                                                                                       b_dec,
                                                                                                       c_dec,
                                                                                                       d_dec,
                                                                                                       e_dec,
                                                                                                       f_dec,
                                                                                                       g_dec,
                                                                                                       h_dec,
                                                                                                       expected_out_dec,
                                                                                                       result_dec)
        if sel == [1, 1, 1]:
            expected_out = h_bin
            expected_out_dec = conversions.bin_arr_to_dec(expected_out)
            assert result == expected_out, 'Error, the input sel: {}, a: {}, b: {}, c: {}, d: {}, e: {}, f: {}, ' \
                                           'g: {}, h: {} should output: {} but instead got: {}'.format(sel_dec,
                                                                                                       a_dec,
                                                                                                       b_dec,
                                                                                                       c_dec,
                                                                                                       d_dec,
                                                                                                       e_dec,
                                                                                                       f_dec,
                                                                                                       g_dec,
                                                                                                       h_dec,
                                                                                                       expected_out_dec,
                                                                                                       result_dec)