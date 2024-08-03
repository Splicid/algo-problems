class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hold = {}

        for num in nums:
            if num not in hold:
                hold[num] = 0
            hold[num] = hold.get(num, 0) + 1
        
        ans = []
        for x in range(k):
            high = max(hold, key=hold.get)
            ans.append(high)
            del hold[high]
        return ans

