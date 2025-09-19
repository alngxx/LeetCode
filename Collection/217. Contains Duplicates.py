class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        '''
        Intuition:
        - Modify list into set
        - If len(set_nums) < len(nums): True
        - Else: False
         '''
        set_nums = set(nums)
        return len(set_nums) < len(nums)
