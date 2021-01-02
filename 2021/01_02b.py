class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# gets the path history from original
def getph(tree, target):
    node = tree
    ph = []
    while 1:
        while node==None:
            # Go to sibling of last 0
            while ph[-1]==1:
                ph.pop()
            ph[-1] = 1
            
            node = tree
            for p in ph:
                if p==0:
                    node = node.left
                else:
                    node = node.right
        if node == target:
            return ph
        else:
            ph.append(0)
            node = node.left
ph = getph(original, target)

# Returns location in cloned tree
node = cloned
for p in ph:
    if p==0:
        node = node.left
    else:
        node = node.right


tree = TreeNode(1)
tree.left = TreeNode(2)
node = tree.left
node.left = TreeNode(3)
node.left.left = TreeNode(4)
node.right = TreeNode(5)
node.right.right = TreeNode(6)

getph(tree, 6)
