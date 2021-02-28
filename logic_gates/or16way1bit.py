from or8way1bit import Or8Way1Bit
from or2way1bit import Or2Way1Bit

class Or16Way1Bit:
    
    def compute(self, _in):

        or8Way1Bit_1 = Or8Way1Bit()
        or8Way1Bit_2 = Or8Way1Bit()

        or8Way1Bit_1_out = or8Way1Bit_1.compute(_in[:8])
        or8Way1Bit_2_out = or8Way1Bit_2.compute(_in[8:])

        or2Way1Bit_1 = Or2Way1Bit()
        return or2Way1Bit_1.compute(or8Way1Bit_1_out, or8Way1Bit_2_out)



        
