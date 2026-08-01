# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sametree (p,q,exact):
            if exact:
                if not p and not q: return True
                if not p or not q: return False
                else:
                    return (p.val == q.val and
                            sametree(p.left,q.left,True)and 
                            sametree(p.right,q.right,True))
            else:
                if not p and q: return False
                if sametree(p,q,True):
                    return True
                return sametree(p.left,q, False) or sametree(p.right,q,False)
        return sametree(root,subRoot,False)
