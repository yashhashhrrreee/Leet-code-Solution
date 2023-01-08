class TrieNode:
    def __init__(self):
        self.children=[None]*26
        self.isending=False
        self.count=0
        self.ind=0

class Solution:
    def __init__(self):
        self.root=TrieNode()

    def longestCommonPrefix(self, strs: List[str]) -> str:


        def insertt(val):
            curr=self.root
            for i in range(len(val)):
                index=ord(val[i])-ord('a')
                if not curr.children[index]:
                    curr.children[index]=TrieNode()
                    curr.count+=1
                    curr.ind=index
                curr=curr.children[index]
            curr.isending=True

        ans=''
        def iteration(ans):
            curr=self.root
            flag=False
            while not curr.isending:
                if curr.count>1:
                    return ans
                elif curr.count==1:
                    ans+=chr(curr.ind+ord('a'))
                    curr=curr.children[curr.ind]
            return ans
        for i in strs:
            insertt(i)
        return iteration(ans)