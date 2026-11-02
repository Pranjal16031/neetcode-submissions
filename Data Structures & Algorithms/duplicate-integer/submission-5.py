class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        arr=sorted(nums)
        for i in range(1,len(nums)):
            if arr[i]==arr[i-1]:
                return bool(1)
        return bool(0)