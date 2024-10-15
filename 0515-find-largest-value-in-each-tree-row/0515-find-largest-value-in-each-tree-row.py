# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return 
        queue = deque([root])
        res = []

        while queue:
            curr_len = len(queue)
            max_ele = float('-inf')
            for i in range(curr_len):
                node = queue.popleft()
                max_ele = max(max_ele, node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            res.append(max_ele)
        
        return res