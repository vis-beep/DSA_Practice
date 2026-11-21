
class Solution:
    def findSubtreeSizes(self, parent: list[int], s: str) -> list[int]:
        n = len(parent)

        # Build the original tree
        children = [[] for _ in range(n)]

        for i in range(1, n):
            children[parent[i]].append(i)

        # Store the nearest ancestor for each character
        last = {}

        # New parent array
        new_parent = [-1] * n

        def dfs(node):
            ch = s[node]

            # Find closest ancestor with same character
            if ch in last:
                new_parent[node] = last[ch]
            else:
                new_parent[node] = parent[node]

            # Save current node as nearest ancestor
            old = last.get(ch, -1)
            last[ch] = node

            # Process original children
            for child in children[node]:
                dfs(child)

            # Restore ancestor information
            if old == -1:
                del last[ch]
            else:
                last[ch] = old

        dfs(0)

        # Build the modified tree
        new_children = [[] for _ in range(n)]

        for i in range(1, n):
            new_children[new_parent[i]].append(i)

        # Calculate subtree sizes
        answer = [1] * n

        def calculate(node):
            for child in new_children[node]:
                calculate(child)
                answer[node] += answer[child]

        calculate(0)

        return answer
