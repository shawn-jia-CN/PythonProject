"""
33. 搜索旋转排序数组
整数数组 nums 按升序排列，数组中的值 互不相同 。
在传递给函数之前,nums 在预先未知的某个下标 k(0 <= k < nums.length)上进行了 向左旋转，使数组变为 [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）。
例如， [0,1,2,4,5,6,7] 下标 3 上向左旋转后可能变为 [4,5,6,7,0,1,2] 。
给你 旋转后 的数组 nums 和一个整数 target ，如果 nums 中存在这个目标值 target ，则返回它的下标，否则返回 -1 。
你必须设计一个时间复杂度为 O(log n) 的算法解决此问题。
"""

def rawBinarySearch(nums: list[int], left: int, right: int, target: int) -> int:
    if left >  len(nums) - 1:
        return -1
    if right > len(nums) - 1:
        return -1
    if left < 0:
        return -1
    if right < 0:
        return -1
    if left == right and nums[left] != target:
        return -1
    leftVal = nums[left]
    rightVal = nums[right]
    if rightVal < leftVal:
        return -1
    mid = (left + right) // 2
    print("rawBinarySearch leftVal = {} rightVal = {} nums[mid] = {} target = {}".format(leftVal, rightVal, nums[mid], target) )
    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        return rawBinarySearch(nums, mid+1 , right, target)
    else:
        return rawBinarySearch(nums, left , mid-1, target)

def binarySearch(nums: list[int], left: int, right: int, target) -> int:
    if left >  len(nums) - 1:
        return -1
    if right > len(nums) - 1:
        return -1
    if left < 0:
        return -1
    if right < 0:
        return -1
    if left == right and nums[left] != target:
        return -1
    leftVal = nums[left]
    rightVal = nums[right]
    if leftVal == target :
        return left
    if rightVal == target:
        return right
    if leftVal < rightVal:
        return rawBinarySearch(nums, left, right, target)
    mid = (left + right) // 2
    print(" binarySearch leftVal = {} rightVal = {} nums[mid] = {} target = {}".format(leftVal, rightVal, nums[mid], target) )
    if nums[mid] == target:
        return mid
    else:
        if nums[mid] > leftVal:
            #mid in up field
            if target > nums[mid]:
                return binarySearch(nums, mid, right, target)
            else:
                if target > leftVal:
                    return rawBinarySearch(nums, left, mid, target)
                else:
                    return binarySearch(nums, mid, right, target)
        else:
            #mid in down filed
            if target < nums[mid]:
                return binarySearch(nums, left, mid, target)
            else:
                if target < rightVal:
                    return rawBinarySearch(nums, mid, right, target)
                else:
                    return binarySearch(nums, left, mid, target)

def search(nums: list[int], target: int) -> int:
    print(nums)
    if len(nums) == 0:
        return -1
    if len(nums) == 1:
        if nums[0] == target:
            return 0
        else:
            return -1
    if len(nums) == 2:
        if nums[0] == target:
            return 0
        elif nums[1] == target:
            return 1
        else:
            return -1
    return binarySearch(nums, 0, len(nums)-1, target)

def run():
    print(search([2,3,5,7,1], 6))

if __name__ == "__main__":
    run()


