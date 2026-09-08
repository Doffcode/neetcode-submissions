# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root: return 
        dum = TreeNode(float('inf'))
        dum.left = root
        def dnode(node,t):
            if not node: return
            print(node.val)
            if node.val < t:
                node.right = dnode(node.right,t)
            elif node.val > t:
                node.left = dnode(node.left,t)
            elif node.val == t:
                if not node.left and not node.right: return None
                if not node.left: return node.right
                if not node.right: return node.left
                c = node.right
                while c.left:
                    c = c.left
                val = c.val
                dnode(node, val)
                node.val = val
                return node
            return node
        dnode(dum, key)
        return dum.left

                
