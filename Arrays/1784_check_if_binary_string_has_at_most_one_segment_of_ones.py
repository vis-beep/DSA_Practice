Technique: Pattern detection / String traversal


class Solution(object):
    def checkOnesSegment(self, s):
        for i in range(len(s) - 1):
            if s[i] == '0' and s[i+1] == '1':
                return False
        return True

OR

'''class Solution:
    def checkOnesSegment(self, s):
        return "01" not in s
'''
