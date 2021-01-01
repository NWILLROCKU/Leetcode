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
            m = len(piece)
            # If piece is a possible match
            try:
                if arr[j:j+m]==piece:
                    j += m
                    pieces.remove(piece)
                    break
            except:
                return False
            if p==len(pieces)-1: # reached last piece without finding a match
                return False
    return True
