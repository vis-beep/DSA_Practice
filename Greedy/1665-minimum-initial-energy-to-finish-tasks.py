class Solution:
    def minimumEffort(self, tasks):
        # Sort by (minimum - actual) descending
        tasks.sort(key=lambda x: (x[1] - x[0]), reverse=True)

        energy = 0
        initial = 0

        for actual, minimum in tasks:
            if energy < minimum:
                initial += (minimum - energy)
                energy = minimum

            energy -= actual

        return initial
