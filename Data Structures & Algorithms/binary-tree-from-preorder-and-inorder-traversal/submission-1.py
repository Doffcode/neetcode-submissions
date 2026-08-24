# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) <=0: return None

        posmap = {}
        for i,n in enumerate(inorder):
            posmap[n] = i
        
        def bt(prel,prer,postl,postr):
            if postr - postl < 0: return None
            if postr - postl == 0: return TreeNode(preorder[prel])
            root = TreeNode(preorder[prel])
            
            ind = posmap[preorder[prel]]
            lenght = ind - postl


            root.left = bt(prel+1,prel+lenght, postl,ind-1)
            root.right = bt(prel+1+lenght,prer, ind+1,postr)
            return root 

        root = bt(0,len(preorder)-1,0,len(preorder)-1)
        return root
