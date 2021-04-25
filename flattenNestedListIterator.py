my_arr = [1, [2, [3, 4]]]

def addAllEle(arr):
    i=0
    while i < len(arr):
        if isinstance(arr[i], list):
            addAllEle(arr[i])
        else:
            mylist.append(arr[i])
        i += 1
        
