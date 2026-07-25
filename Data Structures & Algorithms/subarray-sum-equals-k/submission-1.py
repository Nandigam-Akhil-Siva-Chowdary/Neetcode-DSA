class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        cur_sum = 0
        prefix_map = {0:1}
        for num in nums:
            cur_sum += num
            diff = cur_sum - k
            count += prefix_map.get(diff, 0)

            prefix_map[cur_sum] = prefix_map.get(cur_sum,0) + 1
        return count