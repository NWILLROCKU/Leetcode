class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        As = A.copy()
        Bs = B.copy()
        As.sort()
        Bs.sort()
        
        A2 = [-1]*len(A)
        prev_Bs = -1
        while len(As) > 0:
            # get i
            if Bs[-1]==prev_Bs:
                i = prev_i + B[prev_i+1:].index(Bs[-1]) + 1
            else:
                i = B.index(Bs[-1])
            
            if As[-1] > Bs[-1]:
                A2[i] = As.pop()
            else:
                A2[i] = As.pop(0) # use smallest value
            prev_Bs = Bs.pop()
            prev_i = i
        return A2
