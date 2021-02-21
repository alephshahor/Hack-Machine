import pytest
from hack_machine.logic_gates.and2way16bit import And2Way16Bit
from hack_machine.utils import conversions
from random import randrange

n_iterations = 100
n_bit = 16
random_ceil = conversions.bin_to_dec('1' * 16)

and2Way16Bit = And2Way16Bit()

def test_and2way16bit():
    for i in range(n_iterations):
        a_dec = randrange(random_ceil)
        b_dec = randrange(random_ceil)

        a_bin = conversions.dec_to_bin_arr(n_bit, a_dec)
        b_bin = conversions.dec_to_bin_arr(n_bit, b_dec)

        expected_result = conversions.dec_to_bin_arr(n_bit, a_dec & b_dec)
        actual_result = and2Way16Bit.compute(a_bin, b_bin)
        assert actual_result == expected_result, 'Error, a[{}], b[{}] should output: [{}] but got: [{}]'.format(a_bin, b_bin, expected_result, actual_result)