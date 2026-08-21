# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev  = -float('inf')
        def inorder(node):
            nonlocal prev
            if not node: return True 
            left = inorder(node.left)
            if prev >= node.val or not left:
                return False
            else:
                prev =  node.val
            return inorder(node.right)
        return inorder(root)

