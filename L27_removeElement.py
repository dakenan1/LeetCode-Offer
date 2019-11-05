class Solution:
    #def removeElement(self, nums: List[int], val: int) -> int:
    def removeElement(self, nums, val):           #首尾指针交换
        if not nums: return len(nums)       # if not val： 若val == 0，为真
        star = 0
        end = len(nums) - 1
        while star != end:
            if nums[star] == val:
                nums[end], nums[star] = nums[star], nums[end]
                end -= 1
            else: star += 1
        if nums[star] == val: return star
        else: return star+1
    # def removeElement(self, nums, val):          #快慢指针交换
    #     if not nums or: return len(nums)
    #     star = 0
    #     end = 0
    #     while end < len(nums):
    #         if nums[end] == val:
    #             end += 1
    #         else:
    #             nums[star] = nums[end]
    #             star += 1
    #             end += 1
    #     return star
