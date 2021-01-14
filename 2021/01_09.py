# To make a tree one node at a time
class Node:
    def __init__(self, val, children=[]):
        self.val = val
        self.children = []

def goToNext(tree):
    # Go to next node with unexplored kids
    if len(ph)==0:
        return 1 # flag to exit While loop
    
    node = tree
    for i in range(len(ph)-1):
        node = node.children[ph[i]]
        
    try:
        return node.children[ph[-1]+1]
    except:
        ph.pop()
        goToNext(tree)
        # node doesn't have any other kids, so go to parent node


beginWord = 'hit'
wordList = ['hot', 'dot', 'log', 'dog', 'lot']
words = wordList.copy()
wordLength = len(beginWord)
    
# Construct tree for beginWord
ph = [] # Path history showing lineage, starting with root node
tree1 = Node(beginWord)
node = tree1
nodeList = [tree1]
while len(words) > 0:

    # Check each of the remaining words, see if they are a kid of the current node
    i = 0
    parentWord = node.val
    while i < len(words):
        word = words[i]
        diffSum = 0 # sum of different letters
        for j in range(wordLength):
            if word[j] != parentWord[j]:
                diffSum += 1
        if diffSum==1:
            words.remove(word)
            node.children.append(Node(word))
        else:
            i += 1

    # If there are kids, go to the first one            
    if len(node.children) > 0:
        node = node.children[0]
        if node==1:
            break
    else:
        node = goToNext(tree1)
        
##tree.children.append(Node('why'))
##tree.children.append(Node('bye'))
##
### To make a tree all at once
##class Node:
##    def __init__(self, name, children=[]):
##        self.children = children
##        self.name = name
##def createTree():
##    return Node(1,[Node(2,[Node(5),Node(6,[Node(10)])]),Node(3,[Node(7,[Node(11),Node(12)])]),Node(4,[Node(8,[Node(13)]),Node(9,[Node(14)])])])

##def printNode(node):
##    print(node.val)
##    if len(node.children) > 0:
##        for childNode in node.children:
##            printNode(childNode)
