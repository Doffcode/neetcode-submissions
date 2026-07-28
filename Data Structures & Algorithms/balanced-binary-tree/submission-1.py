# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        ret = True
        def dep (node) ->int:
            nonlocal ret
            if not node:return 0
            else:
                lh = dep(node.left)
                rh = dep(node.right)
                if abs(lh-rh) > 1: ret = False
                return max(lh,rh)+1
        dep(root)
        return ret