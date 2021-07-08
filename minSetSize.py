# 26 / 31 test cases passed

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        cnt = []
        uni = []
        for n in arr:
            if n in uni:
                i = uni.index(n)
                cnt[i] += 1
            else:
                i = 0
                while i < len(uni) and n > uni[i]:
                    i += 1
                if i==len(uni):
                    uni.append(n)
                    cnt.append(1)
                else:
                    uni.insert(i, n)
                    cnt.insert(i, 1)
        arrLen = len(arr)
        
        cnt.sort(reverse=True)
        totCnt = cnt[0]
        i = 1
        
        while totCnt < arrLen / 2:
            totCnt += cnt[i]
            i += 1
        return i
