class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        s=0
        san=0
        for i in range(len(gain)):
            d=s+gain[i]
            s=d
            if d>san:
                san=d
                
        return san