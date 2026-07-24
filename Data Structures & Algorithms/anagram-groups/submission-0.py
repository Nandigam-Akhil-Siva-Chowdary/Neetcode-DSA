from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            sorted_strs = "".join(sorted(s))
            res[sorted_strs].append(s)
        return list(res.values())