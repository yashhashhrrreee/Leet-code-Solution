class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        heap = intervals
        heapq.heapify(intervals)
        heapq.heappush(heap, newInterval)
        stack = [  ]
        while len(heap):
            out_s, out_e = heapq.heappop(heap)
            if len(stack) and stack[-1][1] >= out_s:
                stack_s, stack_e = stack.pop()
                stack.append( [stack_s, max(stack_e, out_e)] )
            else:
                stack.append( [out_s, out_e] )
        return stack
    