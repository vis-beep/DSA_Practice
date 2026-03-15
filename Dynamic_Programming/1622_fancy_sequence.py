class Fancy:

    def __init__(self):
        self.MOD = 10**9 + 7
        self.arr = []
        self.mul = 1
        self.add = 0

    def append(self, val: int) -> None:
        # Normalize the value before storing
        val = (val - self.add) % self.MOD
        val = val * pow(self.mul, self.MOD - 2, self.MOD) % self.MOD
        self.arr.append(val)

    def addAll(self, inc: int) -> None:
        self.add = (self.add + inc) % self.MOD

    def multAll(self, m: int) -> None:
        self.mul = (self.mul * m) % self.MOD
        self.add = (self.add * m) % self.MOD

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.arr):
            return -1
        return (self.arr[idx] * self.mul + self.add) % self.MOD
