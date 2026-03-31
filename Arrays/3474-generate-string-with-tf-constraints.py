"""
Problem: Generate String with T/F Constraints

Given:
- str1: string of 'T' and 'F'
- str2: target substring

Construct the lexicographically smallest string such that:
- If str1[i] == 'T' → substring at i matches str2
- If str1[i] == 'F' → substring at i does NOT match str2

Approach:
1. Apply all 'T' constraints first (force matches)
2. Fill remaining positions with 'a' (smallest lexicographically)
3. Precompute substring matches
4. For 'F', break matches minimally while preserving 'T'

Time Complexity: O(n * m * 26)
Space Complexity: O(n + m)
"""


class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)

        # Result array
        word = ['?'] * (n + m - 1)

        # Step 1: Apply 'T' constraints
        for i in range(n):
            if str1[i] == 'T':
                for j in range(m):
                    if word[i + j] == '?' or word[i + j] == str2[j]:
                        word[i + j] = str2[j]
                    else:
                        return ""  # conflict

        # Step 2: Fill remaining with 'a'
        for i in range(len(word)):
            if word[i] == '?':
                word[i] = 'a'

        # Step 3: Precompute matches
        match = [False] * n
        for i in range(n):
            match[i] = True
            for j in range(m):
                if word[i + j] != str2[j]:
                    match[i] = False
                    break

        # Step 4: Fix 'F' constraints
        for i in range(n):
            if str1[i] == 'F' and match[i]:

                changed = False

                # Try modifying from right (min lexicographic impact)
                for j in range(m - 1, -1, -1):
                    pos = i + j
                    original = word[pos]

                    for c in range(ord('a'), ord('z') + 1):
                        c = chr(c)
                        if c == original:
                            continue

                        word[pos] = c

                        # Update only affected windows
                        start = max(0, pos - m + 1)
                        end = min(n - 1, pos)

                        valid = True
                        for k in range(start, end + 1):
                            ok = True
                            for x in range(m):
                                if word[k + x] != str2[x]:
                                    ok = False
                                    break
                            match[k] = ok

                            if str1[k] == 'T' and not ok:
                                valid = False
                                break

                        # Check if successfully broken
                        if valid and not match[i]:
                            changed = True
                            break

                        word[pos] = original  # revert

                    if changed:
                        break

                if not changed:
                    return ""

        return "".join(word)
