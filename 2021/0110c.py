        instMin = min(instructions)
        instMax = max(instructions)
        if instMin==instMax:
            return 0
        cost = 0
        num = []
        cnt = []
        for i in instructions:
            if len(num)==0:
                num = [i]
                cnt = [1]
            elif i < num[0]:
                num.insert(0, i)
                cnt.insert(0, 1)
            elif i > num[-1]:
                num.append(i)
                cnt.append(1)
            else: # num[0] <= i <= num[-1]
                j = 0
                while i > num[j]:
                    j += 1
                # i <= num[j]
                numL = sum(cnt[0:j])
                if i==num[j]:
                    numG = sum(cnt[j+1:len(num)])
                    cnt[j] += 1
                else:
                    numG = sum(cnt[j:len(num)])
                    num.insert(j, i)
                    cnt.insert(j, 1)
                cost += min(numL, numG)
        return cost
