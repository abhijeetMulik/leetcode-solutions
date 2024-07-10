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

        def helper(node, total):
            ans = 0
            if node:
                total += node.val
                ans = dic[total - targetSum]
                dic[total] += 1

                left = helper(node.left, total)
                right = helper(node.right, total)
                ans += left + right
                dic[total] -= 1
                
            
            return ans
        
        return helper(root, 0)
            
   
        