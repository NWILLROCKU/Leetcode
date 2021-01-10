# To make a tree one node at a time
class Node:
    def __init__(self, val, children=[]):
        self.val = val
        self.children = []
tree = Node("hi")
tree.children.append(Node('why'))
tree.children.append(Node('bye'))

# To make a tree all at once
class Node:
    def __init__(self, name, children=[]):
        self.children = children
        self.name = name
def createTree():
    return Node(1,[Node(2,[Node(5),Node(6,[Node(10)])]),Node(3,[Node(7,[Node(11),Node(12)])]),Node(4,[Node(8,[Node(13)]),Node(9,[Node(14)])])])

##def printNode(node):
##    print(node.val)
##    if len(node.children) > 0:
##        for childNode in node.children:
##            printNode(childNode)
