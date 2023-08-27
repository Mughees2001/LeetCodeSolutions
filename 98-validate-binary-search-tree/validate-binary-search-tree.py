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
        values = inOrderTraversal(root)
        for i in range(1, len(values)):
            if values[i] <= values[i - 1]:
                return False
        return True

def inOrderTraversal(root):
        if root is None:
            return []
        return inOrderTraversal(root.left) + [root.val] + inOrderTraversal(root.right)