class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = len(strs)
        a = {}

        for i in range(n):
            temp = list(strs[i])
            print(temp)
            temp.sort()
            temp2 = "".join(temp)

            if temp2 in a:
                a[temp2].append(strs[i])
            else:
                a[temp2] = [strs[i]]

        return list(a.values())