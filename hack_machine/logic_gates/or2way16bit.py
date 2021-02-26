from hack_machine.logic_gates.or2way1bit import Or2Way1Bit

class Or2Way16Bit:

    def compute(self, a, b):

        assert len(a) == 16
        assert len(b) == 16

        or2Way1Bit = Or2Way1Bit()

        result = [0] * 16
        for i in range(16):
            result[i] = or2Way1Bit.compute(a[i],b[i])

        return result
