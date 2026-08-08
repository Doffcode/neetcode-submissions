# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insert(self,node,val):
            if not node:return None
            if not node.left and not node.right:
                if node.val < val:
                    node.right = TreeNode(val)
                else: node.left = TreeNode(val)
                return 
            if node.val < val:
                if node.right:
                    return self.insert(node.right,val)
                else: 
                    node.right = TreeNode(val)
                    return 
            if node.val > val:
                if node.left:
                    return self.insert(node.left,val)
                else: 
                    node.left = TreeNode(val)
                    return root
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root: return TreeNode(val)
        self.insert(root,val)
        return root