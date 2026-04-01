class Solution:
    def survivedRobotsHealths(self, positions, healths, directions):
        """
        Simulates collisions between robots moving on a line.

        Args:
            positions (List[int]): Positions of robots
            healths (List[int]): Health values of robots
            directions (str): Movement directions ('L' or 'R')

        Returns:
            List[int]: Health of surviving robots in original order
        """

        n = len(positions)

        # Combine robot data with original indices
        robots = []
        for i in range(n):
            robots.append((positions[i], healths[i], directions[i], i))

        # Sort robots by position
        robots.sort()

        stack = []  # stores indices of right-moving robots
        alive = [True] * n
        health = healths[:]  # mutable copy

        for pos, h, d, idx in robots:
            if d == 'R':
                stack.append(idx)
            else:
                # Process collisions
                while stack and alive[idx]:
                    top = stack[-1]

                    if health[top] < health[idx]:
                        alive[top] = False
                        stack.pop()
                        health[idx] -= 1

                    elif health[top] > health[idx]:
                        alive[idx] = False
                        health[top] -= 1

                    else:
                        alive[top] = False
                        alive[idx] = False
                        stack.pop()
                        break

        # Collect surviving robots in original order
        result = []
        for i in range(n):
            if alive[i]:
                result.append(health[i])

        return result


# Example usage
if __name__ == "__main__":
    sol = Solution()
    positions = [3, 5, 2, 6]
    healths = [10, 10, 15, 12]
    directions = "RLRL"
    
    print(sol.survivedRobotsHealths(positions, healths, directions))
