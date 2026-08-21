# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def vbs (node,minl,maxr) -> bool:
            if not node: return True
            l = node.left.val if node.left else -float('inf')
            r = node.right.val if node.right  else float('inf')
            maxr = max(maxr,node.val)
            minl = min(minl,node.val)
            return (minl<node.val<maxr) and vbs(node.left,minl,node.val) and vbs(node.right,node.val,maxr)
        return vbs(root,-float('inf'),float('inf'))