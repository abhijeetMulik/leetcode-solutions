# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:

            def inorder(node):
                if not node:
                    return None
                
                inorder(node.left)
                sorted_arr.append(node.val)
                inorder(node.right)

                # val <= q
            def largets_value(q):
                left, right = 0, len(sorted_arr) - 1
                closest = -1
                while left <= right:
                    mid = (left + right) // 2
                    if sorted_arr[mid] <= q:
                        left = mid + 1
                        closest = sorted_arr[mid]
                    else:
                        right = mid - 1
                return closest
            
               # val >= q
            def smallest_value(q):
                left, right = 0, len(sorted_arr) - 1
                closest = -1
                while left <= right:
                    mid = (left + right) // 2
                    if sorted_arr[mid] >= q:
                        right = mid - 1
                        closest = sorted_arr[mid]
                    else:
                        left = mid + 1
                return closest

            sorted_arr = []
            inorder(root)
            ans = []
            for q in queries:
                ans.append([largets_value(q), smallest_value(q)])

            return ans