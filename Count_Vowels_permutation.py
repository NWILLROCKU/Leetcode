class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD = 1e9 + 7
        
        cur = [1]*5
        for i in range(1,n):
            prev = cur.copy()
            cur[0] = (prev[1] + prev[2] + prev[4]) % MOD
            cur[1] = (prev[0] + prev[2]) % MOD
            cur[2] = (prev[1] + prev[3]) % MOD
            cur[3] = (prev[2]) % MOD
            cur[4] = (prev[2] + prev[3]) % MOD
        return int( sum(cur) % MOD )
