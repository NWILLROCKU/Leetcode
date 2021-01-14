        instMin = min(instructions)
        instMax = max(instructions)
        if instMin==instMax:
            return 0
        cost = 0
        nums = []
        for i in instructions:
            j = 0
            numL = 0
            while j < len(nums):
                if nums[j] >= i:
                    numL = j
                    break
                j += 1
            if j==len(nums):
                nums.append(i)
                continue
            insertion_j = j
            numG = 0
            while j < len(nums):
                if nums[j] > i:
                    numG = len(nums)-j
                    break
                j += 1
            cost += min(numL, numG)
            nums.insert(insertion_j, i)
        return cost
