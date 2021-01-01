height = [1,8,6,2,5,4,8,3,7]
n = len(height)
area_max = 0
i1_max = 0
i2_max = 0
for i1 in range(n-1):
    i2 = i1 + 1
    while i2 < n:
        area= (i2-i1)*min(height[i1], height[i2])
        if area > area_max:
            i1_max = i1
            i2_max = i2
            area_max = area
        i2 += 1
