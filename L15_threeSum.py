class Solution:
    #def threeSum(self, nums: List[int]) -> List[List[int]]:
    def threeSum(self, nums):
        re = []
        #nums = list(set(nums))
        if len(nums) < 3: return re
        nums = sorted(nums)
        i = 0
        j = 1
        k = len(nums) - 1
        while i < len(nums)-2:
            if nums[i] > 0:
                break
            if j >= k or nums[k] < 0 or (i > 0 and nums[i]==nums[i-1]):
                i += 1
                j = i + 1
                k = len(nums) - 1
                continue 
        
            if nums[i] + nums[j] + nums[k] == 0:
                # if [nums[i], nums[j], nums[k]] not in re:      #超时
                #     re.append([nums[i], nums[j], nums[k]])
                if j-1 > i:
                    if nums[j] != nums[j-1]: re.append([nums[i], nums[j], nums[k]])
                elif k < len(nums)-1:
                    if nums[k] != nums[k+1]: re.append([nums[i], nums[j], nums[k]])
                else:
                    re.append([nums[i], nums[j], nums[k]])
                j += 1
                k -= 1
            elif nums[i] + nums[j] + nums[k] < 0:
                j += 1
            else:
                k -= 1

        return re
