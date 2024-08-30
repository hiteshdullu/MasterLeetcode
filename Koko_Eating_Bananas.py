class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        i = 1
        j = max(piles)
        ans = 0
        while i <= j:
            mid = (i+j)//2
            hours = self.hours_taken(piles, mid)
            if hours <= h:
                ans = mid
                j = mid-1
            else:
                i = mid+1
        return ans
    
    def hours_taken(self, piles, speed):
        hours = 0
        for i in piles:
            hours = hours + ceil(i/speed)
        return hours
