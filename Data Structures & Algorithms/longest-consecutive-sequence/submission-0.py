class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sets = set(nums)
        n = len(nums)
        res = 0
        for num in sets:
            if num -1 not in sets:
                length = 1
                current = num

                while current +1 in sets:
                    length +=1 
                    current +=1 

                res = max(res,length)

                
        return res