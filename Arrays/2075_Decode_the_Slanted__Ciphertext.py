💡 Approach

Key Observations
The encoded text is stored row-wise, so we can rebuild the matrix.
Original text was written diagonally, so we reverse that:
Traverse diagonals starting from first row.

🛠️ Algorithm

Compute number of columns:

cols = len(encodedText) // rows
Rebuild matrix row-wise
Traverse diagonally:
Start from (0, col)
Move (i+1, j+1)
Remove trailing spaces

#Code

class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        # Edge case
        if rows == 1:
            return encodedText
        
        n = len(encodedText)
        cols = n // rows
        
        # Step 1: Build matrix
        matrix = []
        idx = 0
        for r in range(rows):
            matrix.append(encodedText[idx:idx + cols])
            idx += cols
        
        # Step 2: Traverse diagonals
        result = []
        
        for start_col in range(cols):
            i, j = 0, start_col
            while i < rows and j < cols:
                result.append(matrix[i][j])
                i += 1
                j += 1
        
        # Step 3: Remove trailing spaces
        return "".join(result).rstrip()
