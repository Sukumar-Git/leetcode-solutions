class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n
        
        while left <= right:
            mid = left + (right - left) // 2
            res = guess(mid)
            
            if res == 0:
                return mid
            elif res == -1:
                # Your guess is higher than the picked number
                right = mid - 1
            else:
                # Your guess is lower than the picked number
                left = mid + 1
        
        return -1