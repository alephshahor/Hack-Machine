

class Decoder:

    def compute(self, instr):
        assert len(instr) == 16

        x = instr[0]

        a = instr[3]

        c1 = instr[4]
        c2 = instr[5]
        c3 = instr[6]
        c4 = instr[7]
        c5 = instr[8]
        c6 = instr[9]

        d1 = instr[10]
        d2 = instr[11]
        d3 = instr[12]

        j1 = instr[13]
        j2 = instr[14]
        j3 = instr[15]

        return x, a, c1, c2, c3, c4, c5, c6, d1, d2, d3, j1, j2, j3