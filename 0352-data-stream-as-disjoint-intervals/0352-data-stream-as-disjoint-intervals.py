class SummaryRanges:

    def __init__(self):
        self.nums = []

    def addNum(self, value: int) -> None:
        idx = bisect.bisect_left(self.nums, value, key=lambda x: x[0])
        if idx > 0:
            # If value can merge with behind
            if self.nums[idx - 1][1] >= value: return
            if self.nums[idx - 1][1] + 1 == value:
                self.nums[idx - 1][1] = value
                # Check if behind can merge with current
                if idx < len(self.nums) and value + 1 == self.nums[idx][0]:
                    self.nums[idx - 1][1] = self.nums[idx][1]
                    self.nums = self.nums[:idx] + self.nums[idx + 1:]
                return
            # If value can merge with current
            if idx < len(self.nums) and value >= self.nums[idx][0]: return
            if idx < len(self.nums) and value + 1 == self.nums[idx][0]:
                self.nums[idx] = [value, self.nums[idx][1]]
                return
            self.nums = self.nums[:idx] + [[value, value]] + self.nums[idx:]
        else:
            if idx < len(self.nums) and value + 1 == self.nums[idx][0]:
                self.nums[idx] = [value, self.nums[idx][1]]
            elif len(self.nums) == 0 or value < self.nums[idx][0]:
                self.nums = [[value, value]] + self.nums

    def getIntervals(self) -> List[List[int]]:
        return self.nums


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()