from collections import deque

class Solution:
    def removeInvalidParentheses(self, s):
        
        def isValid(string):
            count = 0

            for ch in string:
                if ch == '(':
                    count += 1
                elif ch == ')':
                    count -= 1

                    # Too many closing parentheses
                    if count < 0:
                        return False

            return count == 0

        queue = deque([s])
        visited = {s}
        result = []

        found = False

        while queue:
            current = queue.popleft()

            # If valid, this is the minimum-removal level
            if isValid(current):
                result.append(current)
                found = True

            # Don't generate strings with more removals
            # after finding valid answers
            if found:
                continue

            # Remove one parenthesis at every position
            for i in range(len(current)):
                if current[i] not in "()":
                    continue

                new_string = current[:i] + current[i + 1:]

                if new_string not in visited:
                    visited.add(new_string)
                    queue.append(new_string)

        return result
