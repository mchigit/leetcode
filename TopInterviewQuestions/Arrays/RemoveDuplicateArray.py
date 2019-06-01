"""
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Given nums = [0,0,1,1,1,2,2,3,3,4],

Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.

It doesn't matter what values are set beyond the returned length.




The idea of the solution:

Let the number of unique numbers = n. We are return n and making sure nums[0:n] are filled with these unique number
If the array is only 1 element, just return 1
so we basically have 2 pointers, 1 loops through the array, and 1 as counter. Counter = 0
When encounter a number different than nums[counter], perform swap. Counter += 1

At the end, return counter + 1

"""


def removeDuplicates(nums) -> int:
    if not nums:
        return 0

    if len(nums) == 1:
        return 1

    counter = 0
    indexReplace, indexLoop = 0, 0
    while indexLoop < len(nums):
        if nums[indexLoop] != nums[indexReplace]:
            indexReplace += 1
            nums[indexReplace] = nums[indexLoop]
            counter += 1
        indexLoop += 1

    return counter + 1


if __name__ == "__main__":
    nums = [0,0,1,1,1,2,2,3,3,4]
    length = removeDuplicates(nums)
    print(length)
    for i in range(length):
        print(nums[i])

