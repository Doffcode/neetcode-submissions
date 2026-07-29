# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def bbt(node) -> int:
            if not node:
                return 0
            lh = bbt(node.left)
            rh = bbt(node.right)
            if lh == -1 or rh == -1 or abs(lh-rh) >1:
                return -1
            else: return max(lh,rh) +1
        return bbt(root) != -1