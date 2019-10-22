class Solution:
    def twoSum(self, nums, target):
        if not nums:
            return 
        for j in range(len(nums)-1):
            for k in range(1,len(nums)-j):
                if nums[j] == target - nums[j+k]:
                    return [j,j+k]
        return


"""         
        if not nums:
            return 
        left = []
        query = []
        for i in range(len(nums)):
            if nums[i] <= target:
                left.append(nums[i])
                query.append(i)
        for j in range(len(left)-1):
            for k in range(1,len(left)-j):
                if nums[j] == target - nums[j+k]:
                    return [query[j],query[j+k]]
        return """