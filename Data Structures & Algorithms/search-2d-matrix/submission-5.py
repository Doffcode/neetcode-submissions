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
        left ,right= 0,len(matrix[rowh])-1
        while(left <= right):
            mid = (left+right)//2
            if matrix[rowh][mid] < target:
                left = mid+1
            elif matrix[rowh][mid] > target:
                right = mid-1
            else:
                return True
        return False
                
                
