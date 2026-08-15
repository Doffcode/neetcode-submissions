class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ret = []
        stk = deque()
        stk.append(root)
        while stk:
            n = len(stk)
            carr = []
            for _ in range (n):
                node = stk.popleft()
                if node:
                    carr.append(node.val)
                    stk.append(node.left)
                    stk.append(node.right)
            if carr: ret.append(carr)
        return ret