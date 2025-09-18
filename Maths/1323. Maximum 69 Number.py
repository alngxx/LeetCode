class Solution:
    def maximum69Number(self, num: int) -> int:
        '''
        Intuition:
        Turn num into list of its digit for mutable
        When find the first 6, turn it to 9
        Finally, join the digit in string type to new_num
        '''

        digit = list(str(num))

        for i in range(len(digit)):
            if digit[i] == '6':
                digit[i] = '9'
                break

        new_num = int(''.join(digit))
        return new_num
