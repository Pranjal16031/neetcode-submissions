class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums=sorted(nums)
        l=len(nums)
        answer=[]
        for i in range(0,l):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left=i+1
            right=l-1
            target=-nums[i]
            while left < right:
                if nums[right]+nums[left]==target:
                    answer.append([nums[i],nums[left],nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif nums[right]+nums[left]>target:
                    right=right-1
                else:
                    left=left+1
        return answer