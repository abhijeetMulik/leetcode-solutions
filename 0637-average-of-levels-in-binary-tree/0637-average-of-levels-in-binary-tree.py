# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        ans = []
        if not root:
            return ans
        q = deque([root])
        while q:
            level = len(q)
            tmp = []
            count = 0
            for i in range(level):
                node = q.popleft()
                tmp.append(node.val)
                count += 1
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(sum(tmp)/count)
        return ans

        