# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return
        queue = deque([root])
        res = []
        isLeft = True

        while queue:
            curr_len = len(queue)
            tmp = []
            for i in range(curr_len):
                node = queue.popleft()
                tmp.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
            if isLeft:
                res.append(tmp)
                isLeft = False
            else:
                res.append(tmp[::-1])
                isLeft = True
        
        return res


        