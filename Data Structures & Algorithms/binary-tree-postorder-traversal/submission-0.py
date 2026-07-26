# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stk = []
        stk.append([root,False])
        res = []
        while stk:
            cur,tag = stk.pop()
            if not cur:
                continue
            if tag == True:
                res.append(cur.val)
            else:
                stk.append([cur,True])
                stk.append([cur.right,False])
                stk.append([cur.left,False])
        return res