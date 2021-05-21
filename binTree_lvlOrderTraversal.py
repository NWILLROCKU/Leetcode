# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root==None:
            return []
        
        nextNodes = [root]
        valList = []
        while nextNodes:
            curNodes = nextNodes
            
            curVals = []
            nextNodes = []
            for node in curNodes:
                curVals.append(node.val)
                if node.left:
                    nextNodes.append(node.left)
                if node.right:
                    nextNodes.append(node.right)
                    
            valList.append(curVals)
        return valList
