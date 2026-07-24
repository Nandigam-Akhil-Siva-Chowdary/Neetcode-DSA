class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        majority_count = len(nums) // 2
        for num in nums:
            count[num] = count.get(num, 0) + 1
            if count[num] > majority_count:
                return num
        