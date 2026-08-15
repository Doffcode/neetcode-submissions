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
            if len(carr)>0: ret.append(carr)
            if len(narr)>0: stk.append(narr)
        return ret