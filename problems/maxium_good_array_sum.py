"""
https://leetcode.com/problems/maximum-good-subarray-sum/solutions/4893884/python-solution-with-o-n/

Approch suffix sum

"""


def maximumSubarraySum( nums: list[int] , k: int) -> int:
    sums = dict()
    current_sum = 0
    max_sum = float("-inf")

    for value in nums:

        # check if 
        if value - k in sums:
            min_val = sums[value - k]
            max_sum = max(max_sum, current_sum + value - min_val)

        if value + k in sums:
            min_val = sums[value + k]
            max_sum = max(max_sum, current_sum + value - min_val)

        sums[value] = min(sums.get(value, float("inf")), current_sum)
        current_sum += value

    return max_sum if max_sum != float("-inf") else 0



maximumSubarraySum([1,2,3,4,5,6], 1)
