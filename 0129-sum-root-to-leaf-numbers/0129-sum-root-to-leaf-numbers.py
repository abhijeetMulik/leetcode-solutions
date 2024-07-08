# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = []
        def helper(node, ans):
            if not node:
                return 

            ans +=str(node.val)
            
            if not (node.left or node.right):
                res.append(ans)
                return
            
            helper(node.left, ans)
            helper(node.right, ans)

        helper(root, "")
        total = 0

        for r in res:
            total += int(r)

        return total

            

        