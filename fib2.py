class Solution:
    def fib(self, n: int) -> int:
        prev = 0
        num = 1
        if n==0:
            return prev
        elif n==1:
            return num
        else:
            for i in range(n-1):
                prevprev = prev
                prev = num
                num = prev + prevprev
            return num
