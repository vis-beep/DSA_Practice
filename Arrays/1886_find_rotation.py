class Solution:
    def findRotation(self, mat, target):
        """
        Check if matrix 'mat' can be rotated (0°, 90°, 180°, 270°)
        to match the 'target' matrix.
        """

        n = len(mat)

        def rotate(matrix):
            """Rotate matrix 90 degrees clockwise"""
            return [[matrix[n - j - 1][i] for j in range(n)] for i in range(n)]

        for _ in range(4):
            if mat == target:
                return True
            mat = rotate(mat)

        return False
