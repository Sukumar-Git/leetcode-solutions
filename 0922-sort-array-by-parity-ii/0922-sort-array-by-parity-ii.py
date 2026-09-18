class Solution:
    def sortArrayByParityII(self, nums: list[int]) -> list[int]:
        even, odd = 0, 1
        n = len(nums)
        
        while even < n and odd < n:
            # Find the first misplaced element at an even index
            if nums[even] % 2 == 0:
                even += 2
            # Find the first misplaced element at an odd index
            elif nums[odd] % 2 != 0:
                odd += 2
            else:
                # Both are misplaced, swap them
                nums[even], nums[odd] = nums[odd], nums[even]
                even += 2
                odd += 2
                
        return nums