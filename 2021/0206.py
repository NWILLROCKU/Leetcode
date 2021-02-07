class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.right = TreeNode(4)
root.left.right = TreeNode(5)

def goToNext(node, ancestors):
    # Go up through tree
    if node==ancestors[-1].right and ancestors[-1].left != None:
        # Go to sibling
        return ancestors[-1].left
    else: 
        # Go to parent
        node = ancestors.pop()
        return goToNext(node, ancestors)

    
rightNums = [root.val]
ancestors = []
node = root
while 1:
    # Go down through tree
    if node.right != None:
        ancestors.append(node)
        node = node.right
    elif node.left != None:
        ancestors.append(node)
        node = node.left
        
    # node has no children
    else: 
        try:
            node = goToNext(node, ancestors)
        except:
            break
            
    if len(ancestors)==len(rightNums):
        rightNums.append(node.val)
