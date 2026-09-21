class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        # Expected sum of numbers from 0 to n
        expected_sum = n * (n + 1) // 2
        # Actual sum of elements in the array
        actual_sum = sum(nums)
        # The difference is the missing number
        return expected_sum - actual_sum