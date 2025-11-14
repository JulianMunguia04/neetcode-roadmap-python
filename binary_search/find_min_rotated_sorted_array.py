class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            res = nums[m]
            if nums[r] < nums[l]:
                l = l + 1
            else: 
                r = r - 1
            
            if res > nums[m]:
                res = nums[m]
        return res