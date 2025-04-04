class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        f = [0] + flowerbed + [0]
        i = 1
        while i < len(f)-1:
            if f[i] == 1:
                i += 2
            elif f[i-1] == 0 and f[i] == 0 and f[i+1] == 0:
                f[i] = 1
                n -= 1
                i += 2
            else:
                i += 1
        return n <= 0