class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        noDuplicates = set()
        for i in range(len(nums)):
            if nums[i] in noDuplicates:
                return True
            noDuplicates.add(nums[i])
        return False
    
#Time Complexity O(n), n being the count of numbers in nums. ie Linear Time