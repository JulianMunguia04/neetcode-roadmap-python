class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        solution_row = False
        rl, rr = 0, len(matrix) - 1
        mid = (rl + rr) // 2
        x, y = 0, len(matrix[mid]) - 1
        while rl <= rr:
            mid = (rl + rr) // 2
            if matrix[mid][x] <= target and matrix[mid][y] >= target:
                solution_row = matrix[mid]
                break
            elif matrix[mid][x] < target:
                rl = mid + 1
            elif matrix[mid][y] > target:
                rr = mid -1 
        if not solution_row:
            return False
        l, r = 0, len(solution_row) - 1
        while l <= r:
            mid = (l+r) // 2
            if solution_row[mid] > target:
                r = mid - 1
            elif solution_row[mid] < target:
                l = mid + 1
            else: 
                return True
        return False