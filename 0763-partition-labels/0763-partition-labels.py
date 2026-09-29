class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        # Step 1: Record the last occurrence index of each character
        last_occurrence = {char: i for i, char in enumerate(s)}
        
        result = []
        start = 0
        end = 0
        
        # Step 2: Iterate through the string to form partitions
        for i, char in enumerate(s):
            # Extend the current partition's end to the farthest last occurrence seen so far
            end = max(end, last_occurrence[char])
            
            # If our current index matches the end of the partition, we can make a cut
            if i == end:
                result.append(end - start + 1)
                start = end + 1
                
        return result