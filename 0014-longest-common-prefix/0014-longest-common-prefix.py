class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        
        # Assume the first string is the prefix
        prefix = strs[0]
        
        for s in strs[1:]:
            # Shrink the prefix until it matches the start of string s
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
                    
        return prefix