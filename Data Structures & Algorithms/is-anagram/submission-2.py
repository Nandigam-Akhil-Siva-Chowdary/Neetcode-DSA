class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i] not in t:
                return False
            if s.count(s[i]) != t.count(s[i]):
                return False
        return True