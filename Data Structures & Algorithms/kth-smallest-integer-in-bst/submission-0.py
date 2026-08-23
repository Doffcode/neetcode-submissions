class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root: return None
        count = 0
        ret = 0
        def inorder(node):
            nonlocal count
            nonlocal ret
            if not node: return
            if node.left:inorder(node.left)
            if count == k-1:
                ret = node.val
            count+=1
            if node.right:inorder(node.right)
        inorder(root)
        return ret