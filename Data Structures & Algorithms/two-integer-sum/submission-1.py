class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for i, n in enumerate(nums):
            if target-n not in seen:
                seen[n]=i
            else:
                return [seen[target-n], i]
        