# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        
        if not root:
            return res

        def helper(node, ans):
            if not node:
                return 
            ans.append(node.val)
            if not node.left and not node.right:
                if sum(ans) == targetSum:
                    res.append(list(ans))
            
            helper(node.left, ans)
            helper(node.right, ans)
            ans.pop()
            return
        
        helper(root, [])
        return res

        