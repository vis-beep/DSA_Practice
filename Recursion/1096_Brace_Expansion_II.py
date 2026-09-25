class Solution:
    def braceExpansionII(self, expression):
        def parse(i):
            result = set()
            current = {""}

            while i < len(expression) and expression[i] != "}":

                # Union
                if expression[i] == ",":
                    result.update(current)
                    current = {""}
                    i += 1

                # Nested expression
                elif expression[i] == "{":
                    sub_set, i = parse(i + 1)

                    # Cartesian product / Concatenation
                    new_set = set()

                    for a in current:
                        for b in sub_set:
                            new_set.add(a + b)

                    current = new_set

                # Single character
                else:
                    new_set = set()

                    for word in current:
                        new_set.add(word + expression[i])

                    current = new_set
                    i += 1

            # Add the last expression
            result.update(current)

            # Skip closing brace
            if i < len(expression) and expression[i] == "}":
                i += 1

            return result, i

        result, _ = parse(0)

        return sorted(result)
