class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        arr, dic1, dic2 = s.split(" "), {}, {}
        for i in range(len(arr)):
            if arr[i] not in dic1.keys():
                dic1[arr[i]] = [i]
            else :
                dic1[arr[i]].append(i)

        arr = list(pattern)
        for i in range(len(arr)):
            if arr[i] not in dic2.keys():
                dic2[arr[i]] = [i]
            else :
                dic2[arr[i]].append(i)
        return sorted([v for v in dic1.values()]) == sorted([v for v in dic2.values()])
