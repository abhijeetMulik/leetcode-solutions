# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        def helper(node, maxx, minn):
            if not node:
                return maxx - minn

            maxx = max(maxx, node.val)
            minn = min(minn, node.val)
            left = helper(node.left, maxx, minn)
            right = helper(node.right, maxx, minn)

            return max(left, right)
        return helper(root, root.val, root.val)