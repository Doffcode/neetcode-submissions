# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        nodeval = {}
        self.msum = 0


        # def von(node):
        #     if not node: return 0
        #     if node in nodeval: return nodeval[node]
        #     left = von(node.left.left) + von(node.left.right) if node.left else 0
        #     right = von(node.right.left) + von(node.right.right) if node.right else 0
        #     nodeval[node] = node.val + left + right
        #     return node.val + left + right

        def loot(node,cval): 
            if not node: return 0
            if node in nodeval: s1 = nodeval[node]
            else :
                s1 = cval + node.val
                if node.left: s1+=loot(node.left.left,cval) + loot(node.left.right,cval)
                if node.right: s1+=loot(node.right.left,cval) + loot(node.right.right,cval)
                nodeval[node] = s1
            s2 = cval 
            s2 += loot(node.left,cval) + loot(node.right,cval)
            return max (s1,s2)
        
        return loot(root,0)
            # take path

            # not take path

        #if take path returns more value then then not take path then well take where it is taken or else well not take that also the value 
        #if a node will be it value form top to that node not form that node to the leaf
        #so well start at (root,0) then the take path will be cval+root.val then + loot(left ke bacche,cval) + loot (right ke bacche,cval)
        #then well see the not take path which will be loot(left,)