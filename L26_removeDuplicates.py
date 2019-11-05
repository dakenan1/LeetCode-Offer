class Solution:
    #def removeDuplicates(self, nums: List[int]) -> int:   #要求只能有O(1)的空间操作，以及提示只会打印返回数量的列表长度
    def removeDuplicates(self, nums): 
        if not nums: return 0
        elif len(nums) == 1: return 1
        star = 0
        end = 1
        while end < len(nums):
            if nums[star] == nums[end]: end += 1
            else:
                if end - star < 2:
                    star += 1
                    end += 1
                else:
                    star += 1
                    end += 1
                    nums[star] = nums[end-1]
        return star+1