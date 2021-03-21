i = len(path)-2
while i > 0:
    if path[i-1 : i+2] == '/./' :
        break
    i -= 1
    
folderList = []
folder = ''
i += 1
readingWord = 0
while i < len(path):
    if path[i] != '/':
        if readingWord==0:
            readingWord = 1
        folder += path[i]
    elif readingWord==1:
        readingWord = 0
        
        if folder=='..':
            # Go up a directory, if possible
            if len(folderList) > 0:
                folderList.pop()
        else:
            folderList.append(folder)
            
        folder = ''
        
    i += 1

path2 = ''
for f in folderList:
    path2 += '/' + f
