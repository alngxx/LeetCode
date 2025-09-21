class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []

        for i in range(1, n + 1):
            FizzBuzz = (i % 15 == 0)
            Fizz = (i % 3 == 0 and i % 5 != 0)
            Buzz = (i % 5 == 0 and i % 3 != 0)

            if Fizz:
                ans.append("Fizz")
            elif Buzz:
                ans.append("Buzz")
            elif FizzBuzz:
                ans.append("FizzBuzz")
            else:
                ans.append(str(i))

        return ans
