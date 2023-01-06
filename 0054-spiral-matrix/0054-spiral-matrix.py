class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        def remove_row(matrix, ix):
            return matrix.pop(ix)
        def remove_col(matrix, ix):
            return [x.pop(ix) for x in matrix]
        res = []
        for _ in range(len(matrix)):
            try:
                res += remove_row(matrix, 0)
                res += remove_col(matrix, -1)
                res += reversed(remove_row(matrix, -1))
                res += reversed(remove_col(matrix, 0))
            except IndexError:
                break
        return res
        