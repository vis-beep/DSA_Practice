class Solution:
    def maxNumberOfFamilies(self, n, reservedSeats):
        rows = {}

        # Store reserved seats for each affected row
        for row, seat in reservedSeats:
            if row not in rows:
                rows[row] = set()
            rows[row].add(seat)

        # All rows without reservations can fit 2 groups
        answer = (n - len(rows)) * 2

        # Process only rows having reservations
        for seats in rows.values():

            left = not any(seat in seats for seat in [2, 3, 4, 5])
            middle = not any(seat in seats for seat in [4, 5, 6, 7])
            right = not any(seat in seats for seat in [6, 7, 8, 9])

            if left and right:
                answer += 2
            elif left or middle or right:
                answer += 1

        return answer
