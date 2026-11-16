# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        goodNodes = 0
        def dfs(root, maxVal):
            if not root:
                return None
            nonlocal goodNodes
            if root.val >= maxVal:
                maxVal = root.val 
                goodNodes += 1
            dfs(root.left, maxVal)
            dfs(root.right, maxVal)
        dfs(root, root.val)   
        return goodNodes                                                                    