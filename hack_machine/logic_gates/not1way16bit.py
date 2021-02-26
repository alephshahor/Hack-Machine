from hack_machine.logic_gates.not1way1bit import Not1Way1Bit

class Not1Way16Bit:

    def compute(self, in_):

        assert len(in_) == 16

        not1Way1Bit = Not1Way1Bit()
        result = [0] * len(in_)

        for i in range(len(in_)):
            result[i] = not1Way1Bit.compute(in_[i])

        return result
