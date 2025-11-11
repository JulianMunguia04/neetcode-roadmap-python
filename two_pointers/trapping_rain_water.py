class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        lMax, rMax = height[0], height[r]
        waterCount = 0
        while l <= r:
            if lMax <= rMax:
                if  0 <= min(lMax, rMax) - height[l]:
                    waterCount += (min(lMax, rMax) - height[l])
                if lMax < height[l]:
                    lMax = height[l]
                l += 1
            else:
                if  0 <= min(lMax, rMax) - height[r]:
                    waterCount += (min(lMax, rMax) - height[r])
                if rMax < height[r]:
                    rMax = height[r]
                r -= 1
        return waterCount                        


