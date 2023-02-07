class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left=0
        right=10000000
        mid=(left+right)//2
        while(True):
            temp=mid
            if mid*mid>x:
                right=mid+1
            else:
                left=mid
            mid=(left+right)//2
            if temp==mid:
                break
        return left
        