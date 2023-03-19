class TrieNode:
    def __init__(self):
        self.childrens=defaultdict(TrieNode)
        self.isEnd=False
class WordDictionary:

    def __init__(self):
        self.root=TrieNode()
        
    def addWord(self, word: str) -> None:
        root=self.root
        for c in word:
            root=root.childrens[c]
        root.isEnd=True
    def searchHelper(self,root,word):
        for i,char in enumerate(word):
            if char=='.':
                for child in root.childrens:
                    if self.searchHelper(root.childrens[child],word[i+1:]):
                        return True
                return False
            else:
                if char in root.childrens:
                    root=root.childrens[char]
                else:
                    return False
        return root.isEnd==True
            
        
    def search(self, word: str) -> bool:
        return self.searchHelper(self.root,word)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)