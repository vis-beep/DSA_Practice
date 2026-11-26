
class Solution:
    def canAliceWin(self, n: int) -> bool:
        remove = 10
        alice = True

        while n >= remove:
            n -= remove
            remove -= 1
            alice = not alice

        return not alice
