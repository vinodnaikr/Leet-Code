class Fancy:
    def __init__(self):
        self.vals = []
        self.a = 1  # Multiplier
        self.b = 0  # Increment
        self.MOD = 10**9 + 7

    def append(self, val: int) -> None:
       
        inv_a = pow(self.a, self.MOD - 2, self.MOD)
        self.vals.append(((val - self.b) * inv_a) % self.MOD)

    def addAll(self, inc: int) -> None:
        self.b = (self.b + inc) % self.MOD

    def multAll(self, m: int) -> None:
        self.a = (self.a * m) % self.MOD
        self.b = (self.b * m) % self.MOD

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.vals):
            return -1
        return (self.a * self.vals[idx] + self.b) % self.MOD