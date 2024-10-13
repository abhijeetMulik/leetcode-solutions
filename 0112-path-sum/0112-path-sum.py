# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, count):
            if node == None:
                return False
            
            if node.left == None and node.right == None:
                return count + node.val == targetSum
            
            left = dfs(node.left, count + node.val)
            right = dfs(node.right, count + node.val)
        
            return left or right
        return dfs(root, 0)

