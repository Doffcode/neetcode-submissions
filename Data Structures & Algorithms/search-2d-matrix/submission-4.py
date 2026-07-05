class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rowl = 0
        rowh = len(matrix)-1
        while rowl<rowh:
            rowmid = (rowl+rowh)//2
            if matrix[rowmid][0] < target:
                if matrix[rowmid][-1] > target:
                    rowh = rowmid
                    break
                elif matrix[rowmid][-1] < target:
                    rowl = rowmid+1
                else:
                    return True
            elif matrix[rowmid][0] > target:
                rowh = rowmid-1
            else:
                return True
        for n in matrix[rowh]:
            if n == target:
                return True
        return False
                
                
