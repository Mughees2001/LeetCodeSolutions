# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        values = inorder_traversal(root)
        for i in range(1, len(values)):
            if values[i] <= values[i - 1]:
                return False
        return True

def inorder_traversal(root):
        if root is None:
            return []
        return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right)