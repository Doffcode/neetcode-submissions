# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findnode(self,node,key) ->bool:
        if not node: return False
        else:
            return (node.val == key or 
            self.findnode(node.left,key) or 
            self.findnode(node.right,key))
#------------------------------------------------------------------
    def findp(self, node, key) -> TreeNode:
        if not node: return
        if node.left and node.left.val == key:
            return node
        if node.right and node.right.val == key:
            return node
        left_res = self.findp(node.left, key)
        if left_res:
            return left_res
        return self.findp(node.right, key)
#---------------------------------------------------------------------------------
    def findsucc(self,node):
        if not node: return None
        l = node.left
        r = node.right
        if not l and not r:
            return None
        elif not l and r:
            succ = r
            while succ.left: succ = succ.left
            return succ
        elif not r and l:
            succ = l
            while succ.right: succ = succ.right
            return succ
        else:
            succ = l
            while succ.right: succ = succ.right
            return succ
#---------------------------------------------------------------------------------
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not self.findnode(root,key): return root
        if not root: return None

        parent = self.findp(root,key)
        if not parent:
            if not root.left and not root.right: return None
            else:
                succ = self.findsucc(root)
                value = succ.val
                succp = self.findp(root,value)
                print (succp.val,succ.val)
                print(succ,succp.left,succp.right)
                if succp.left and succp.left== succ:
                    succp.left = None
                else: succp.right = None
                root.val = value
                return root
        if parent.left and parent.left.val == key:node = parent.left
        else: node = parent.right
        # ------- check if leaf---------
        if not node.left and not node.right:
            if parent.left == node:
                parent.left = None
            else: parent.right = None
        else:
        #------------not leaf node -- then its succ must exits------
            succ = self.findsucc(node)
            value = succ.val
            succp = self.findp(node,value)
            print (succp.val,succ.val)
            print(succ,succp.left,succp.right)
            if succp.left and succp.left== succ:
                succp.left = None
            else: succp.right = None
            node.val = value
        return root









