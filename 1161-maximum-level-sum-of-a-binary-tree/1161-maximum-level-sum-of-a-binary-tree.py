# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        heap = []
        level = 0
        while queue:
            curr_len = len(queue)
            total = 0
            level += 1
            for i in range(curr_len):
                node = queue.popleft()
                total += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            heapq.heappush(heap, (-total, level))
        
        return heapq.heappop(heap)[1]


        