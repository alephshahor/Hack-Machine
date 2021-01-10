

class DMux2Way16Bit:

    def compute(self, sel, _in):

        assert len(_in) == 16

        zero = [0] * 16
        
        if sel == 0:
            return [_in, zero]
        else:
            return [zero, _in]
