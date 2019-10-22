class Solution:
    #def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    def findMedianSortedArrays(self, nums1, nums2):              # 复杂度为O(m+n)，不到O(log(m+n))
        i = 0
        j = 0
        re = []
        while nums1 and nums2:
            if nums1[0] > nums2[0]: 
                re.append(nums2.pop(0))                 
            elif nums1[0] < nums2[0]: 
                re.append(nums1.pop(0))
            else: 
                re.append(nums1.pop(0))
                re.append(nums2.pop(0))
            # if len(re) > 1:                   #要求re不允许有相等的数
            #     if re[-1] == re[-2]: re.pop()
        if nums1: re += nums1
        if nums2: re += nums2

        if len(re)%2 == 0:
            return (re[len(re)//2-1] + re[len(re)//2])/2.0
        else:   
            return re[len(re)//2]/1.0