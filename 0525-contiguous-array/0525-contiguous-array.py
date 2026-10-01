class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count_map = {0: -1}  # Base case: running sum of 0 occurs before index 0
        max_len = 0
        running_sum = 0
        
        for i, num in enumerate(nums):
            # Treat 1 as +1 and 0 as -1
            running_sum += 1 if num == 1 else -1
            
            if running_sum in count_map:
                # Same prefix sum found -> equal number of 0s and 1s in subarray
                max_len = max(max_len, i - count_map[running_sum])
            else:
                # Store first occurrence index of this prefix sum
                count_map[running_sum] = i
                
        return max_len