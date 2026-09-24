from collections import Counter

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # Step 1: Count the occurrences of each number
        count = Counter(nums)
        
        # Step 2: Create frequency buckets (index = frequency, value = list of numbers)
        freq = [[] for _ in range(len(nums) + 1)]
        for num, cnt in count.items():
            freq[cnt].append(num)
            
        # Step 3: Collect top k elements from buckets in reverse order (highest frequency first)
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res