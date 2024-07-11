# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        maximal = float("-inf")
        q = deque([root])
        ans = 0
        lvl = 0
        while q:
            level = len(q)
            tmp = 0
            lvl += 1
            for i in range(level):
                node = q.popleft()
                tmp += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if tmp > maximal:
                ans = lvl
                maximal = tmp
            
        return ans
        