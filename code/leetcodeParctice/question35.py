"""
35. 搜索插入位置
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
请必须使用时间复杂度为 O(log n) 的算法。
"""

def binarySearch(nums: list[int], left: int, right: int, target: int) -> int:
    if left == right:
        if nums[left] == target:
            return left
        else:
            left + 1
    if left > right:
        return right + 1
    mid = (left + right) // 2
    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        return binarySearch(nums, mid + 1, right, target)
    else:
        return binarySearch(nums, left, mid-1, target)

def searchInsert(nums: list[int], target: int) -> int:
    if len(nums) == 0:
        return 0
    if nums[0] >= target:
        return 0
    if nums[len(nums) - 1] < target:
        return len(nums)
    if nums[len(nums) - 1] == target:
        return len(nums) - 1
    return binarySearch(nums, 0, len(nums) - 1, target)


def run():
    print(searchInsert([1,3,5,6], 7))

if __name__ == "__main__":
    run()