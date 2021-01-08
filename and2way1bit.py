
class And2Way1Bit:
    def compute(self, _in):

        assert len(_in) == 2

        a = _in[0]
        b = _in[1]

        if a == 1 and b == 1:
            return 1
        else:
            return 0
