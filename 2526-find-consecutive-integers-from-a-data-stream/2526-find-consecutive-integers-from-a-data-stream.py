class DataStream:

    def __init__(self, value: int, k: int):
        self.value,self.k=value,k
        self.count=self.prev_val=None
    
    def consec(self, num: int) -> bool:
        if self.prev_val==num==self.value:
            if self.count<self.k:self.count+=1
            if self.count==self.k :return True
            return False
        self.prev_val,self.count=num,1
        if self.count==self.k and num==self.value:return True
        return False

# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)