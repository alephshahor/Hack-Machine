
class Not1Way1Bit:

    def compute(self, _in):

        assert len(_in) == 1

        return int(not(_in[0]))
