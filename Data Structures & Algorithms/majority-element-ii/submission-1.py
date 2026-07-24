class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        num_dict = {}
        nums_set = set(nums)
        final_nums = []
        k = len(nums) / 3
        for num in nums_set:
            count = nums.count(num)
            if count > k:
                final_nums.append(num)
        return final_nums