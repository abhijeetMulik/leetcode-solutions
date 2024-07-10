# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        dic = defaultdict(int)
        dic[0] = 1

        def helper(node, curr):
            ans = 0
            if node:

                curr += node.val
                ans = dic[curr - targetSum]
                dic[curr] += 1
                left = helper(node.left, curr)
                right = helper(node.right, curr)
                ans += left + right

                dic[curr] -= 1
            
            return ans    

        return helper(root, 0)     
        