class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Initialize pointers
        p1 = m - 1
        p2 = n - 1
        tail = m + n - 1
        
        # While there are elements to process in both arrays
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[tail] = nums1[p1]
                p1 -= 1
            else:
                nums1[tail] = nums2[p2]
                p2 -= 1
            tail -= 1
            
        # If any elements remain in nums2, copy them over
        # (If elements remain in nums1, they are already in place)
        while p2 >= 0:
            nums1[tail] = nums2[p2]
            p2 -= 1
            tail -= 1