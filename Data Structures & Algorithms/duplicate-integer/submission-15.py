class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        

        #one liner for this question
        return (len(set(nums)) != len(nums) )
