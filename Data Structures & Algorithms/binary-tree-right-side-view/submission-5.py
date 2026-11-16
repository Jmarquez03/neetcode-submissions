# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = collections.deque([root])
        res = []
        while q:
            while q and not q[-1]:
                q.pop()
            qlen = len(q)
            if qlen == 0:
                return res
            res.append(q[-1].val)
            for i in range(qlen):
                node = q.popleft()
                if not node:
                    continue
                q.append(node.left)
                q.append(node.right)
        return res
