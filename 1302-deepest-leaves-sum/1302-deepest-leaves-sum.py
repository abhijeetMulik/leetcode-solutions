# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        ans = 0
        if not root:
            return ans
        q = deque([root])
        while q:
            level = len(q)
            lis = []
            for i in range(level):
                node = q.popleft()
                lis.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans = sum(lis)
        return ans


        