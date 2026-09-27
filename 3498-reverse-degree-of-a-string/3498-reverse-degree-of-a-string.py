class Solution:
    def reverseDegree(self, s: str) -> int:
        total_degree = 0
        for i, char in enumerate(s):
            # 1-indexed position in the string
            index_in_string = i + 1
            # Position in the reversed alphabet ('a' = 26, 'b' = 25, ..., 'z' = 1)
            index_in_reversed_alphabet = 26 - (ord(char) - ord('a'))
            
            total_degree += index_in_reversed_alphabet * index_in_string
            
        return total_degree