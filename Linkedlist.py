class Node:
    
    def __init__(self, name, children=[]):
        self.children = children
        self.name = name

def equalsOne(n):
    if n==1:
        return True
    else:
        return False

