from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        result = []
        a=[]

        for key, count in c.most_common(k):
            result.append(key)
            a.append(count)
  
        return result