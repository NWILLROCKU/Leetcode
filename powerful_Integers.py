class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        def getp(x, bound):
            if x==1:
                return [1]
            pow=1
            p1=[]
            while pow <= bound-1:
                p1.append(pow)
                pow *= x
            return p1
        
        p1 = getp(x, bound)
        p2 = getp(y, bound)
        
        powInt=[]
        for i in p1:
            for j in p2:
                if i+j <= bound:
                    if i+j not in powInt:
                        powInt.append(i+j)
                else:
                    break
        return powInt
            
