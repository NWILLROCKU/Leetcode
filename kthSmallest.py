class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        if k==1:
            return matrix[0][0]
        
        n = len(matrix)
        if k==n**2:
            return matrix[-1][-1]
        
        def addMaybe():
            if maybe not in coords:
                coords.append(maybe)
                explored.append( matrix[maybe[0]][maybe[1]] )
        
        coords = [(0,0)]
        explored = [matrix[0][0]]
        
        i = 0
        while i < k:
            j = explored.index(min(explored))
            i += 1
            ith_smallest = explored[j]
            #print(ith_smallest)
            
            old_coords = coords.pop(j)
            explored.pop(j)
            if old_coords[0] + 1 < n:
                maybe = (old_coords[0] + 1, old_coords[1])
                addMaybe()
            if old_coords[1] + 1 < n:
                maybe = (old_coords[0], old_coords[1] + 1)
                addMaybe()
        return ith_smallest
            
