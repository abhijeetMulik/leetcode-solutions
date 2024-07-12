# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        values = []
        def helper(node):
            if not node:
                return
            
            helper(node.left)
            values.append(node.val)
            helper(node.right)
        
        helper(root)
        ans = 0
        tmp = float('inf')
        # ans[0] = float('inf')
        # target = round(target)

        for i in values:
            if abs(target - i) <= tmp:
                if tmp != abs(target - i):
                    tmp = abs(target - i)
                    ans = i

        return ans

        