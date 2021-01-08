from not1x1 import Not1x1 

class Not16x16:
    def compute(self, in_):
        not1x1 = Not1x1()
        result = [0] * len(in_)
        for i in range(len(in_)):
            result[i] = not1x1.compute(in_[i])
        return result
            

        
