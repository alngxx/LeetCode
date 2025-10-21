class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        square = n ** 2

        lst = [j for i in grid for j in i]  # list of all elements
        s = set(lst)  # set of all elements

        res = [-1] * 2
        res[0] = sum(lst) - sum(s)  # duplicate number i.e. a
        res[1] = square * (square + 1) // 2 - sum(s)  # missing number i.e. b

        return res