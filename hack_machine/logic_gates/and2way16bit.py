from hack_machine.logic_gates.and2way1bit import And2Way1Bit

class And2Way16Bit:
    def compute(self, a, b):

        assert len(a) == 16
        assert len(b) == 16

        and2Way1Bit = And2Way1Bit()

        result = [0] * 16
        for i in range(16):
            result[i] = and2Way1Bit.compute(a[i], b[i])

        return result
