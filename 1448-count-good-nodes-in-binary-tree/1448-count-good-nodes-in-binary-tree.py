# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node, max_val):
           
            if node == None:
                return 0
            
            left = dfs(node.left, max(node.val, max_val))
            right = dfs(node.right, max(node.val, max_val))
            ans = left + right

            if node.val >= max_val:
                ans += 1
            
            return ans
        
        return dfs(root, float('-inf'))
        