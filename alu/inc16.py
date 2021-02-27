from half_adder import HalfAdder

class Inc16:

    def compute(self, _in):

        assert len(_in) == 16

        half_adder = HalfAdder()

        result = [0] * 16
        carry = 1
        for i in range(15, -1, -1):
            sum, carry = half_adder.compute(_in[i], carry)
            result[i] = sum

        return result
