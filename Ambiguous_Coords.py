class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        def get_nums(digits):
            if digits[0]=='0':
                if digits[-1]=='0':
                    if len(digits) > 1:
                        nums = []
                    else:
                        nums = [digits]
                else:
                    nums = [digits[0] + '.' + digits[1:]]
            else:
                if digits[-1]=='0':
                    nums = [digits]
                else:
                    nums = []
                    for dot in range(1, len(digits)+1):
                        if dot==len(digits):
                            nums.append(digits)
                        else:
                            nums.append(digits[:dot] + '.' + digits[dot:])
            return nums
                
        coords = s[1:-1]
        ans = []
        for comma in range(1, len(coords)):
            digits1 = coords[:comma]
            digits2 = coords[comma:]
            nums1 = get_nums(digits1)
            nums2 = get_nums(digits2)
            #print(nums1, nums2)
            for num1 in nums1:
                for num2 in nums2:
                    ans.append('(' + num1 + ', ' + num2 + ')')
        return ans
            
