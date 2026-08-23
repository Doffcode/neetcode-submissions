class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count ,ret = 0, 0

        def inorder(node):
            nonlocal count, ret
            if not node: return
            inorder(node.left)
            if count == k-1: ret = node.val
            count+=1
            inorder(node.right)

        inorder(root)
        return ret