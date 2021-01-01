root = [2,3,1,3,1,None,1]

lvlSize = 1
tree = [root[0]]
lvlCnt = 1
i = 1
while i < len(root):
    if lvlCnt==lvlSize:
        tree.append([])
        lvlCnt = 0
        lvlSize *= 2
    tree[-1].append(root[i])
    lvlCnt += 1
    i += 1
