def arrMadeOfPieces(arr, pieces):
# Returns true if it is possible to form arr by concatenating the
# arrays in pieces in any order; otherwise, returns false

##    pieces = [[1,2],[3,4,5],[6]]
##    arr = [6, 1, 2, 3, 4, 5]
    n = len(arr)
    j= 0
    while j < len(arr):
        if len(pieces)==0: # Ran out of pieces
            return False

        # Search through remaining pieces
        for p in range(len(pieces)):
            piece = pieces[p]

            # If piece is a possible match
            if piece[0]==arr[j]: 
                m = len(piece)

                # Check if all of piece is a match
                i = 1
                j += 1
                while i < m:
                    if j==n: # total elements of pieces > numel(arr)
                        return False
                    elif piece[i]==arr[j]:
                        i += 1
                        j += 1
                    else:
                        break
                if i==m: # the whole piece matched the next section of arr
                    pieces.remove(piece)
                    break # Search for the next piece
            if p==len(pieces)-1: # reached last piece without finding a match
                return False
    return True
