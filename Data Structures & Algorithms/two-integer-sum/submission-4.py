class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        for i in range(len(nums)):
            num=nums[i]
            temp=target-num
            if temp in hashmap:
                return [hashmap[temp],i]
            else:
                hashmap[num]=i
                






















        hashmap={}
        for i in range(len(nums)):
            diff=target-nums[i]
            if diff in hashmap:
                return [hashmap[diff], i]
            else:
                hashmap[nums[i]]=i