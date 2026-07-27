# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        stk = [[root,1]]
        ml = 0
        while stk:
            cur,l = stk.pop()
            ml = max(ml,l)
            if cur.left: stk.append([cur.left,l+1])
            if cur.right: stk.append([cur.right,l+1])
        return ml
