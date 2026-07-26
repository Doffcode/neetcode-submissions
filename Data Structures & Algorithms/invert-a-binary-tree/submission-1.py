# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        exp = []
        exp.append(root)
        if not root: return root
        while exp:
            cur = exp.pop()
            if cur.left and cur.right:
                exp.append(cur.left)
                exp.append(cur.right)
                r = cur.right
                cur.right = cur.left
                cur.left = r
            elif cur.left and not cur.right:
                exp.append(cur.left)
                cur.right = cur.left
                cur.left = None
            elif cur.right and not cur.left:
                exp.append(cur.right)
                cur.left = cur.right
                cur.right = None
            else:
                continue
        return root


