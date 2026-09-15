class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # If target is greater than or equal to the last letter, wrap around to the first
        if target >= letters[-1]:
            return letters[0]
        
        left, right = 0, len(letters) - 1
        
        while left < right:
            mid = (left + right) // 2
            if letters[mid] <= target:
                left = mid + 1
            else:
                right = mid
                
        return letters[left]