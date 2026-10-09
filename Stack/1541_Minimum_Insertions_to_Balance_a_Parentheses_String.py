class Solution:
    def minInsertions(self, s: str) -> int:
        insertions = 0
        open_count = 0

        for ch in s:
            if ch == '(':
                if open_count > 0 and open_count % 1 == 0:
                    open_count += 2
            else:
                open_count -= 1
                if open_count < 0:
                    insertions += 1
                    open_count = 1

        return insertions + open_count
