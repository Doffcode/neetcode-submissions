# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        #check if the nodes childern can become none 
        #then check if the nodes chidernare not there thne we can delete theat node as well
        def dnode(node):
            if not node: return None
            node.left = dnode(node.left)
            node.right = dnode(node.right)
            if not node.left and not node.right and node.val == target: return None
            else: return node
        
        return dnode(root)