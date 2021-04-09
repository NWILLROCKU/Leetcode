class Node(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = Node(1)
root.left = Node(2)
root.left.left = Node(6)
root.right = Node(3)
node = root.right
node.left = Node(4)
node.left.left = Node(8)
node.left.right = Node(9)
node.right = Node(5)
node.right.right = Node(7)

voyage = [1,3,5,7,4,9,8,2,6]

def getNodeList():
    # Returns list of values of nodes visited in pre-order
    node = root
    nL = [node.val]
    rewindFlag = 0
    anc = []
    rev = []
    flipped = []
    while True:
        if node.left==None:
            if node.right==None:
                return [-1]
            else:
                node = node.right
                
        if rewindFlag==1:
            while len(anc) > 0 and node==anc[-1].right:
                node = anc.pop()
            # Now, anc = [] or node==anc[-1].left
            if len(anc)==0:
                return nL
            if anc[-1].right != None: # node has a sibling
                node = anc[-1].right
                nL.append(node.val)
                rewindFlag = 0
            else: # node is an only child
                anc.pop()
        elif node.left != None and :
            anc.append(node)
            node = node.left
            nL.append(node.val)
        elif node.right != None:
            anc.append(node)
            node = node.right
            nL.append(node.val)
        else:
            rewindFlag = 1
    
