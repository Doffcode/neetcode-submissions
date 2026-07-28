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
            if not node:return 0
            else:
                lh = dep(node.left)
                rh = dep(node.right)
                if lh == -1 or rh == -1 or abs(lh-rh)>1: 
                    return -1
                else: return max(lh,rh)+1
        if dep(root) == -1:
            return False 
        else: return True