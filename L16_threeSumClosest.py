class Solution:
    #def threeSumClosest(self, nums: List[int], target: int) -> int:
    def threeSumClosest(self, nums, target):
        if len(nums) < 3: return ''
        nums = sorted(nums)
        i, j, k = 0, 1, len(nums) - 1
        re = 2**31
        while i < len(nums)-2:
            if j >= k or (i > 0 and nums[i]==nums[i-1]):
                i += 1
                j = i + 1
                k = len(nums) - 1
                continue    
            if abs(nums[i] + nums[j] + nums[k] - target) < abs(re - target):  
                re = nums[i] + nums[j] + nums[k]

            if nums[i] + nums[j] + nums[k] - target < 0:
                j += 1
            elif nums[i] + nums[j] + nums[k] - target > 0:
                k -= 1
            else: 
                re = target
                break
        return re