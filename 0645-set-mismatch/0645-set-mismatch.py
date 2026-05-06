class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums = sorted(nums)
        x=0
        for i in range(1, len(nums)+1):
            if(nums.count(i)>1):
                x=i
                break
        a = list(set(list(range(1,len(nums)+1)))-set(nums))[0]
        return [x,a]