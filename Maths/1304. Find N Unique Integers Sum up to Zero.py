class Solution:
    def sumZero(self, n: int) -> List[int]:
        '''
        Intuition:
        Insert n//2 postive integers and their negatives into arr
        If n is even, we have n unique integers.
        Elif n is odd (which now we only got n-1 elements in the arr), insert 0 so total still = 0
        '''
        res = []

        for i in range(1, n // 2 + 1):
            res.append(i)
            res.append(-i)
        if n % 2 == 1:
            res.append(0)

        return res
