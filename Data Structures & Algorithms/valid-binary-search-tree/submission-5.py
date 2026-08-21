# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def inorder(node):
            if not node: return 
            else :
                inorder(node.left)
                ret.append(node.val)
                inorder(node.right)
        ret = []
        inorder(root)
        for i in range(1,len(ret)):
            if ret[i-1] >= ret[i]:
                return False
        return True


