# Last updated: 11/26/2025, 5:40:29 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = 0
        def dfs(node, i):
            nonlocal ans
            
            if node:
                if node.val >= i:
                    ans += 1
                dfs(node.left, max(node.val, i))
                dfs(node.right, max(node.val, i))

        dfs(root, float('-inf'))
        return ans
