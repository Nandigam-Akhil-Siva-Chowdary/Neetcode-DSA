class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        k = len(nums) // 3
        count = {}
        res = []
        for num in nums:
            count[num] = count.get(num, 0)+ 1
        for n, num in count.items():
            if num > k:
                res.append(n)
        return res