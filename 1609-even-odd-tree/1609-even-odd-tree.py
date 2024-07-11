# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        q = deque([root])
        count = 0
        while q:
            level = len(q)
            tmp_even = 0
            tmp_odd = float("inf")
            # print('level :', level)
            for i in range(level):
                node = q.popleft()
                # print('inside for :', node.val)
                if (count % 2 == 0):
                    # print('count % 2 == 0 ', count % 2 == 0)
                    # print('node.val % 2 == 0 ', node.val % 2 == 0)
                    # print('node.val < tmp_even ', node.val < tmp_even)
                    if (node.val % 2 == 0) or (node.val <= tmp_even): #even
                        # print('even', tmp_even, ' ', node.val)
                        # print('count is :', count)
                        return False
                    tmp_even = node.val
                if (count % 2 == 1):
                    if (node.val % 2 == 1) or (tmp_odd <= node.val): #odd
                        # print('odd', tmp_odd, ' ', node.val)
                        return False
                    tmp_odd = node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            count += 1
            # print('count', count)
        return True
