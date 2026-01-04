class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        # Function return all divisors of an integer
        def get_divisor(n):
            divisor = []
            for i in range(1, int(n ** 0.5) + 1):
                if n % i == 0:
                    divisor.append(i)
                    # If i is not square root of n, append it complement divisor
                    if i != n // i:
                        divisor.append(n // i)
            return sorted(divisor)

        # Valid int with exactly four divisors
        total = 0
        for num in nums:
            if len(get_divisor(num)) == 4:
                total += sum(get_divisor(num))
        return total
