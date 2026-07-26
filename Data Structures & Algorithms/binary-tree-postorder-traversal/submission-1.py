# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        exp = []
        coll = []
        res = []
        exp.append(root)
        if not root:
            return coll
        while exp:
            cur = exp.pop()
            coll.append(cur.val)
            if cur.left: exp.append(cur.left)
            if cur.right: exp.append(cur.right)
        while coll:
            res.append(coll.pop())
        return res