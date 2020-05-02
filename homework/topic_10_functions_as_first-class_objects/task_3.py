"""
Write a function called `choose_func` which takes a list of nums and 2 callback functions.
If all nums inside the list are positive, execute the first function on that list and return the result of it.
Otherwise, return the result of the second one
"""

def choose_func(nums1, nums2):
    pass
    def square_nums(nums):
        for num in nums:
            return num ** 2

    def remove_negatives(nums):
        for num in nums:
            if num > 0:
                return nums

nums1 = [1, 2, 3, 4, 5]
nums2 = [1, -2, 3, -4, 5]
choose_func(nums1, nums2)