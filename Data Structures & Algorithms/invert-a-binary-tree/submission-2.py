# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return None
        stk = [root]
        while stk:
            cur = stk.pop()
            cur.left, cur.right = cur.right, cur.left
            if cur.left: stk.append(cur.left)
            if cur.right: stk.append(cur.right)
        return root


