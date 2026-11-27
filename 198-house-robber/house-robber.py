class Solution:
    def rob(self, nums: list[int]) -> int:
        prev2 = 0  # max money robbed up to i - 2
        prev1 = 0  # max money robbed up to i - 1

        for amount in nums:
            current = max(prev1, prev2 + amount)
            prev2 = prev1
            prev1 = current

        return prev1
