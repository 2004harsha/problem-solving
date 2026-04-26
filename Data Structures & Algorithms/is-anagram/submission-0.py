class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq ={}
        for char in s:
            freq[char] = freq.get(char,0) +1

        freqq = {}
        for char in t:
            freqq[char] = freqq.get(char,0) + 1

        return (freq == freqq )