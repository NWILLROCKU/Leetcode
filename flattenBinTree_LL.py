# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root==None:
            return
        branchPts = []
        node = root
        while True:
            # Go to leftmost leaf, identifying branch points along the way
            while node.left != None or node.right != None:
                if node.left != None:
                    if node.right != None:
                        branchPts.append(node)
                    node = node.left
                elif node.right != None:
                    node = node.right
            
            if branchPts==[]:
                break
            # "Cut" tree at last branch point, graft it onto end of LL
            node.right = branchPts[-1].right
            node = node.right
            branchPts.pop()

        # Put the LL in the required format, i.e. right branches only
        node = root
        while node.left != None or node.right != None:
            if node.left != None:
                node.right = node.left
                node.left = None
            node = node.right
                    
