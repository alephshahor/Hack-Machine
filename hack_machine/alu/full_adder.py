from half_adder import HalfAdder
from or2way1bit import Or2Way1Bit

class FullAdder:

    def compute(self, a, b, c):

        half_adder_1 = HalfAdder()
        half_adder_2 = HalfAdder()

        or2Way1Bit = Or2Way1Bit()

        half_adder_1_sum, half_adder_1_carry = half_adder_1.compute(a,b)
        half_adder_2_sum, half_adder_2_carry = half_adder_2.compute(half_adder_1_sum, c)

        total_carry = or2Way1Bit.compute(half_adder_1_carry, half_adder_2_carry)

        return half_adder_2_sum, total_carry
