class Solution:
    def numberOfGoodPaths(self, vals, edges):
        total = n = len(vals)
        dict1 = collections.defaultdict(int)
        freq = [collections.Counter({vals[i]:1}) for i in range(n)]
        edges = sorted([max(vals[i],vals[j]),i,j] for i,j in edges)

        def find(x):
            if x not in dict1:
                return x
            else:
                if x != dict1[x]:
                    dict1[x] = find(dict1[x])
                return dict1[x]

        for val,i,j in edges:
            a, b = find(i), find(j)
            total += freq[a][val]*freq[b][val]
            dict1[b] = a
            freq[a] = collections.Counter({val:freq[a][val] + freq[b][val]})

        return total





        


        






        







