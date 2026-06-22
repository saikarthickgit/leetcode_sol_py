class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a=[]
        c=Counter(nums)
        top_k = c.most_common(k)
        for num, freq in top_k:
            a.append(num)

        return a
        