class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        history = {}
        for i, n in enumerate(nums):
            if n in history:
                return [history[n],i]
            history[target-n] = i
        