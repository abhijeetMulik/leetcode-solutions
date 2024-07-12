# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            root = TreeNode(val)
            return root
        def helper(node, prev_node, val, isLeft):
            if not node:
                node = TreeNode(val)
                if isLeft:
                    prev_node.left = node
                else:
                    prev_node.right = node
                return
            
            if val >= node.val:
                helper(node.right, node, val, False)
            else:
                helper(node.left, node, val, True)
        
        helper(root, root, val, True)
        return root

        