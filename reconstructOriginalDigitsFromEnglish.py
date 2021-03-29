class Solution:
    def originalDigits(self, s: str) -> str:
        cnt = [0] * 10
        f = h = v = o = ii = 0
        for i in s:
            # Actual numbers
            if i=='z':
                cnt[0] += 1
            elif i=='w':
                cnt[2] += 1
            elif i=='u':
                cnt[4] += 1
            elif i=='x':
                cnt[6] += 1
            elif i=='g':
                cnt[8] += 1
            
            # Surrogates
            elif i=='f':
                f += 1
            elif i=='h':
                h += 1
            elif i=='v':
                v += 1
            elif i=='o':
                o += 1
            elif i=='i':
                ii += 1
        cnt[5] = f - cnt[4]
        cnt[3] = h - cnt[8]
        cnt[7] = v - cnt[5]
        cnt[1] = o - cnt[0] - cnt[2] - cnt[4]
        cnt[9] = ii -cnt[5] - cnt[6] - cnt[8]
        
        ans = ''
        for i in range(len(cnt)):
            for j in range(cnt[i]):
                ans += str(i)
        return ans
            
