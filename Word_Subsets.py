class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        answer = []
        
        # Make B2
        B2 = []
        for b in B:
            B2_old = B2.copy()
            for ltr in b:
                if ltr not in B2_old:
                    B2.append(ltr)
                else:
                    B2_old.remove(ltr)
        
        for iA in range(len(A)):
            a = list(A[iA])
            ltr_i = 0
            while ltr_i < len(B2):
                if B2[ltr_i] not in a:
                    break
                else:
                    a.remove(B2[ltr_i])
                ltr_i += 1
            if ltr_i==len(B2):
                answer.append(A[iA])
                
        return answer
