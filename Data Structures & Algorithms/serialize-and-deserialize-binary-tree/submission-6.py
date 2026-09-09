# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        ret = []

        def dfs(node):
            if not node: ret.append("n")
            else:
                ret.append(node.val)
                dfs(node.left)
                dfs(node.right)
        dfs(root)
        rets = ""
        for n in ret: rets+=str(n) + "*"
        return rets
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        nums = [x for x in data.split("*") if x]
        for i,n in enumerate(nums):
            if n != 'n':
                nums[i] = int(n)

        def build():
            if nums[self.ind] == "n": return None
            else:
                node = TreeNode(nums[self.ind])
                self.ind+=1
                node.left = build(self.ind)
                self.ind+=1
                node.right = build(self.ind)
                self.ind+=1
            return node
            root = build
        return root