

class DMux2Way1Bit:

    def compute(self, sel, _in):

        if sel == 0:
            return [_in, 0]
        else:
            return [0, _in]
