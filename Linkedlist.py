class Node:
    
    def __init__(self, name):
        self.val = name
        self.next = None
        
inputList = [1,2,3,4,5]
head = node = Node(inputList[0])
for i in range(1, len(inputList)):
    node.next = Node(inputList[i])
    node = node.next

# Divide LL into pairs. Within each pair, swap the 2 nodes.
i=0
nodesRemaining = len(inputList)-i # number of nodes that haven't been swapped yet
while nodesRemaining > 1:
    # Get addresses of current and next node (node 1 & 2)
    if i==0:
        node1 = head
    else:
        node1 = prevNode.next
    node2 = node1.next
    
    nextNode = node2.next # get address of next-next node

    # Swap nodes 1 & 2
    if i==0:
        head = node2
    else:
        prevNode.next = node2
    node2.next = node1
    node1.next = nextNode

    prevNode = node1
    i += 2
    nodesRemaining = len(inputList)-i

print('Hi GIT!')

