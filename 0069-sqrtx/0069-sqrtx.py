class Solution:
    def mySqrt(self, x: int) -> int:
        r=0
        while True:
            if r**2>x:
                r-=1
                break
            elif r**2==x:
                break
            r+=1
        return r