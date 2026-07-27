# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        dia = 0
        def dep(node) -> int:
            if not node:
                return 0
            else:
                nonlocal dia
                lh = dep(node.left)
                rh = dep(node.right)
                dia = max(lh+rh,dia)
                return max(lh,rh)+1
        dep(root)
        return dia