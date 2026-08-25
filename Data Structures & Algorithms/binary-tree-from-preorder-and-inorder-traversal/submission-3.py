# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) <=0: return None

        idx = {val:i for i, val in enumerate(inorder)}
        self.pre = 0

        def build(low, high):
            if low > high: return None

            root_val = preorder[self.pre]
            self.pre += 1
            mid = idx[root_val]
            root = TreeNode(root_val)
            root.left = build(low,mid-1)
            root.right = build(mid+1,high)
            return root
        
        return build(0, len(preorder)-1)

