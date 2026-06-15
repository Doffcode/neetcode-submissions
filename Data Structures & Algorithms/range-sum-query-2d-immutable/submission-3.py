class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            self.sm = [[0]]
            return
        
        row = len(matrix)
        col = len(matrix[0])
        self.sm = [[0]* (col+1) for _ in range (row+1)]

        for r in range (1,row+1):
            for c in range (1,col+1):
                self.sm[r][c] = matrix[r-1][c-1] + \
                self.sm[r-1][c] + \
                self.sm[r][c-1] - \
                self.sm[r-1][c-1] 
          
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1,row2,col1,col2 = row1+1, row2+1, col1+1, col2+1 
        total = self.sm[row2][col2]
        left = self.sm[row2][col1-1]
        top = self.sm[row1-1][col2]
        topleft = self.sm[row1-1][col1-1]
        return total - left - top + topleft