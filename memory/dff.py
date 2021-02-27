

class DFF:

    def __init__(self):

        self.internal_state = 0

    def compute(self, _in):
        
        previous_state = self.internal_state
        self.internal_state = _in
        return previous_state
