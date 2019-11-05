class Solution:
    #双指针法，务必认真理解移动窄板而不是长板的理论依据！
    #def maxArea(self, height: List[int]) -> int: 
    def maxArea(self, height):
        
        if len(height) <= 1:
            return 0      
        st = 0
        ed = len(height) - 1
        maxs = min(height[ed],height[st])*(ed - st)
        
        while st < ed:
            if height[ed] >= height[st]:            #两个板一样高的时候，移动哪边都可以
                st += 1
            else:
                ed -= 1
            maxs = max(min(height[ed],height[st]) * (ed - st), maxs)
        return maxs
        