class Solution:
    def fib(self, n: int) -> int:
        def myfib(n):
            if n==0:
                return 0
            elif n==1:
                return 1
            else:
                return myfib(n-1) + myfib(n-2)
        return myfib(n)
