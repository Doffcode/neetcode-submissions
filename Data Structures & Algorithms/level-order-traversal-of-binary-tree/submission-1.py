class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ret = []
        stk = deque()
        stk.append([root])
        while stk:
            arr = stk.pop()
            arr.reverse()
            carr = []
            narr = deque()
            while arr:
                element = arr.pop()
                if element:
                    carr.append(element.val)
                    if element.left: narr.append(element.left)
                    if element.right: narr.append(element.right)
            if carr: ret.append(carr)
            if narr: stk.append(narr)
        return ret