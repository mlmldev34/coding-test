class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        return max([i.count('1') for i in list(''.join(list(map(str, nums))).split('0'))])