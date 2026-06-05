class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        row = len(matrix)+1
        col = len(matrix[0])+1 
        self.cusum = [[0] * col for _ in range(row)]
        for i in range (1,row):
            for j in range (1,col):
                self.cusum[i][j] = matrix[i-1][j-1]
        for i in range (1,row):
            for j in range (1,col):
                self.cusum[i][j] = self.cusum[i][j] + self.cusum [i-1][j] +self.cusum [i][j-1]-self.cusum [i-1][j-1]
        print (self.cusum)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = self.cusum[row2+1][col2+1]
        left = self.cusum[row2+1][col1]
        top = self.cusum[row1][col2+1]
        topleft = self.cusum[row1][col1]
        return total + topleft - left - top
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)