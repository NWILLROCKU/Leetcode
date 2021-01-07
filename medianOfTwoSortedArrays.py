nums1 = [1,2]
nums2 = [3,4]

nums1 += nums2
nums1.sort()
m = len(nums1)
if m==0:
    med= []
else:
    
    if m % 2==0:
        med= (nums1[int(m/2)] + nums1[int(m/2)-1]) / 2
    else:
        med= nums1[int((m-1)/2)]

print(med)
