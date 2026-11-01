class Solution:
    def trap(self, height: List[int]) -> int:
        left=0
        right= len(height) - 1
        l_m = 0
        r_m= 0
        w= 0
        while left < right:
            if height[left]< height[right]:
                l_m =max(l_m, height[left])
                w+= l_m - height[left]
                left +=1
            else:
                r_m= max(r_m, height[right])
                w +=r_m - height[right]
                right-= 1
        return w