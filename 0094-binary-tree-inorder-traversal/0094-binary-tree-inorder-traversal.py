# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        t = []
        
        def inorder(root):
            '''
            Traverse the left node to end of tree, add the value, return up a node, try the right traversal. repeat.
            '''
            if root is None:
                return
            # traverse the left node to the end of the tree
            inorder(root.left)
            # append the value of the end node
            t.append(root.val)
            # traverse the right of the tree
            inorder(root.right)
        
        inorder(root)
        
        return t