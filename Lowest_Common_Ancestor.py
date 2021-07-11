class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def check_p_q():
            # Check if p or q encountered
            if path[-1] in nodes:
                paths.append(path.copy())
                nodes.remove(path[-1])
        
        path = [root] # stack showing lineage from root to current node
        branchPts = [] # stack of branching nodes encountered along the way
        nodes = [p,q]
        paths = [] # paths to p, q
        
        check_p_q()
            
        while nodes != []:
            # Go to next leaf (ordered from left -> right), keeping track of nodes passed
            while path[-1].left or path[-1].right:
                # Advance to left leaf
                if path[-1].left:
                    if path[-1].right:
                        branchPts.append(path[-1])
                    path.append(path[-1].left)
                    
                # Advance to right leaf
                elif path[-1].right:
                    path.append(path[-1].right)
                
                check_p_q()
                    
            if nodes==[]:
                break
            
            # Go to right child of last branch point
            while path[-1] != branchPts[-1]:
                path.pop()
            branchPts.pop()
            path.append(path[-1].right)
            
            check_p_q()
        
        # Go through each level of the tree, checking if paths are the same at that level
        level = 0
        while level < len(paths[0]) and level < len(paths[1]) and paths[0][level]==paths[1][level]:
            level += 1
            
        return paths[0][level-1]
