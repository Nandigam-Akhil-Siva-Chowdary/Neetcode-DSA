class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        first_word = strs[0]
        for i, char in enumerate(first_word):
            for ch in strs[1:]:
                if i == len(ch) or ch[i] != char:
                    return first_word[:i]
        return first_word