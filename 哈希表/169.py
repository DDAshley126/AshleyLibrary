class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        times = dict()
        for i in nums:
            times[i] = times.get(i,0) + 1
        for i in set(nums):
            if times.get(i) > (n//2):
                return i