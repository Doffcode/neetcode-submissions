# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.msum = -float("inf")
        
        def calsum(node):
            if not node: return 0
            left = max(calsum(node.left),0)
            right = max(calsum(node.right),0)
            if node.val+left+right > self.msum: self.msum = node.val+left+right
            return max(left,right) + node.val
        calsum(root)
        return self.msum 