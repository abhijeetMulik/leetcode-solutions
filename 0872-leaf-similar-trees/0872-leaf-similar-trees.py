# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        ans1 = []
        ans2 = []
        def helper(node, ans):
            if not node:
                return 
            
            if not node.left and not node.right:
                # print(node.val)
                ans.append(node.val)

            helper(node.left, ans)
            helper(node.right, ans)

            return ans
        
        
       

        return helper(root1, ans1) ==  helper(root2, ans2)

        