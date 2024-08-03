class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        ## Brute Force method
        point1 = 0
        while point1 != len(nums):
            for val in range(point1 + 1, len(nums)):
                ans = nums[point1] + nums[val]
                if ans == target:
                    return [point1, val]
            point1 += 1

        ## Hashmap
        lis = {}
        for idx, val in enumerate(nums):
            math = target - val
            if math in lis:
                return [lis[math], idx]
            lis[val] = idx



