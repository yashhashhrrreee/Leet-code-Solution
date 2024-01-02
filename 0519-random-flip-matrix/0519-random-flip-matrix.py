import random

class Solution:

    def __init__(self, n_rows: int, n_cols: int):
        self.n_rows= n_rows
        self.n_cols = n_cols
        self.start = 0
        self.end = self.n_rows * self.n_cols
        self.pos_dict = collections.defaultdict()
        

    def flip(self) -> List[int]:
        # generate index
        rand_idx = random.randrange(self.start, self.end)
        
        res = self.pos_dict.get(rand_idx, rand_idx)     
        
        # swap - put total at index that we generated
        self.pos_dict[rand_idx] = self.pos_dict.get(self.start, self.start)
        
        # decrease total number of values
        self.start += 1
        
        return [res // self.n_cols, res % self.n_cols]
    
    
    def reset(self) -> None:
        self.pos_dict = collections.defaultdict()
        self.start = 0


# Your Solution object will be instantiated and called as such:
# obj = Solution(m, n)
# param_1 = obj.flip()
# obj.reset()