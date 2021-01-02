def goToNext():
    while ph[-1]==1:
        ph.pop()
    ph[-1] = 1

node = orig
ph = []
while node.val != target:
    if node.left != None:
        ph.append(0)
    else:
        goToNext()
        node = orig
        for p in ph:
            if p==0:
                node = node.left
            else:
                node = node.right
                
# Go to same location in cloned tree

return node
