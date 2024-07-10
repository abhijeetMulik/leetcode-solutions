# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:

        def helper(node, flag, count):
            if node:
                if flag: #left
                    count = max(count, 
                                helper(node.right, False, count + 1),
                                helper(node.left, True, 0)
                    )
                
                else: #right
                    count = max(count, 
                                helper(node.left, True, count + 1),
                                helper(node.right, False, 0)
                    )
                
            return count
        left = helper(root.left, True, 0)
        right = helper(root.right, False, 0)
        return max(left, right)
        