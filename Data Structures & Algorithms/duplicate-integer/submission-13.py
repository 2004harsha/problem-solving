class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq = set()
        for num in nums:
            if(num not in freq):
                freq.add(num)
        if (len(freq) == len(nums)):
            return False
        else :
            return True
