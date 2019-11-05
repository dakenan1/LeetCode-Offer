class Solution:
    #def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
    def fourSum(self, nums, target):     #超时， 利用哈希表记录任意两个相加和，后处理再判断四个数是否重复以及组合是否重复
        leng = len(nums)
        if leng < 4: return [] 
        dict = {} 
        re = []
        for i in range(leng):
            for j in range(i+1,leng):
                dict[(i,j)] = nums[i]+nums[j]
        for k in sorted(dict,key = dict.__getitem__):
            re.append([dict[k],k])
        final = []
        for star in range(len(re)):
            for end in range(star+1,len(re)):
                if re[star][0] + re[end][0] == target and len(set(re[star][1]+re[end][1])) == 4:
                    arr = [nums[re[star][1][0]], nums[re[star][1][1]], nums[re[end][1][0]], nums[re[end][1][1]]]
                    final.append(arr)
        for y in final:
            y.sort()
        final.sort()
        x = 1
        while x < len(final):
            if final[x] == final[x-1]:
                final.pop(x)
            else: x += 1
        return final



