class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # If lengths are different, rotation is impossible
        if len(s) != len(goal):
            return False
        
        # Check if goal is a substring of s + s
        return goal in (s + s)
