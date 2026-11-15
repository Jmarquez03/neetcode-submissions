# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = collections.deque()
        q.append([root])
        res = []
        while len(q) > 0:
            nodeList = []
            valList = []
            checkNodes = q.pop()
            for node in checkNodes:
                if not node:
                    continue
                valList.append(node.val)
                nodeList.append(node.left)
                nodeList.append(node.right)
            if nodeList:
                q.appendleft(nodeList)
            if valList:
                res.append(valList)
        return res
        