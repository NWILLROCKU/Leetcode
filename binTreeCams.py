# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        def goBackOneNode():
            # Backtrack one node, placing cameras as needed
            if watched[-1]==2:
                watched[-2] = 1
            elif watched[-1]==0:
                watched[-1] = 1
                watched[-2] = 2
                numCams += 1
            watched.pop()
            path.pop()
            
        if root==None:
            return 0
        branchPts = []
        path = [root]
        watched = [0]
        numCams = 0
        while True:
            # Go to leftmost leaf, identifying branch points along the way
            while path[-1].left or path[-1].right:
                if path[-1].left:
                    if path[-1].right:
                        branchPts.append(path[-1])
                    path.append(path[-1].left)
                elif path[-1].right:
                    path.append(path[-1].right)
                watched.append(0)

            path.pop()
            watched.pop()
            watched[-1] = 2
            numCams += 1
            
            if branchPts==[]:
                # Go back to root, making sure all nodes along the way are watched
                while len(path) > 1:
                    goBackOneNode()
                return numCams
            else:
                while path[-1] != branchPts[-1]:
                    goBackOneNode()
                branchPts.pop()
                path.append(path[-1].right)
                if watched[-1]==2:
                    watched.append(1)
                else:
                    watched.append(0)
                
