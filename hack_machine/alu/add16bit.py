from full_adder import FullAdder

class Add16Bit:

    def compute(self, a, b):

        assert len(a) == 16
        assert len(b) == 16

        result = [0] * 16
        carry = 0

        full_adder = FullAdder()

        for i in range(15,-1,-1):
            sum, carry = full_adder.compute(a[i],b[i],carry)
            result[i] = sum

        return result
