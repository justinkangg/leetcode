# Last updated: 11/26/2025, 5:41:02 PM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.ans = 0
        self.diameter(root)
        return self.ans

    def diameter(self,node):
        if not node:
            return 0
        left, right = self.diameter(node.left), self.diameter(node.right)
        self.ans = max(self.ans, left + right)

        return 1 + max(left, right)
        
        