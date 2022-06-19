class BaseGenerator:
    def __init__(self):
        self.result = {}
        self._seed()

    def _seed(self):
        raise NotImplementedError("_seed method is not implemented")

    def build(self):
        return self.result
