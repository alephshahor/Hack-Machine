class Or2Way1Bit:

    def compute(self, _in):

        assert len(_in) == 2

        a = _in[0]
        b = _in[1]

        assert len(a) == 1
        assert len(b) == 1

        if a[0] != 0 or b[0] != 0:
            return 1
        else:
            return 0
