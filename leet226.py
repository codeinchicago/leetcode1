#Leetcode 226
#Given the root of a binary tree, invert the tree, and return its root.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #If level is empty, do nothing
        if bool(root) == False:
            return None
        
        #Invert the current level
        root.left, root.right = root.right, root.left

        #Invert the lower levels
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root