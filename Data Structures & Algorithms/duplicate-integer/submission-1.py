class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        arr=[]
        for i in range(0,len(nums)):
            q=nums[0]
            nums.pop(0)
            arr.append(q)
            if arr[i] in nums:
                return bool(1)
        return bool(0)