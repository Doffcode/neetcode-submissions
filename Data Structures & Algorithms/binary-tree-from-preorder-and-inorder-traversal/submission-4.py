# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0: return None
        posmap = {}
        for i,n in enumerate (inorder):
            posmap[n] = i

        self.pre = 0
        
        def build (l,r):
            if l > r: return None

            mid = posmap[preorder[self.pre]]

            self.pre +=1
            
            root = TreeNode(inorder[mid])
            root.left = build(l,mid-1)
            root.right = build(mid+1,r)
            return root

        return build(0, len(preorder)-1) 