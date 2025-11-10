"""
34. 在排序数组中查找元素的第一个和最后一个位置
给你一个按照非递减顺序排列的整数数组 nums,和一个目标值 target。请你找出给定目标值在数组中的开始位置和结束位置。
如果数组中不存在目标值 target,返回 [-1, -1]。
你必须设计并实现时间复杂度为 O(log n) 的算法解决此问题。
"""
def binarySearch(nums: list[int], target: int, left: int , right: int ,ret: list[int]):
    if left > right:
        return 
    if left < 0 or right < 0 or left > len(nums) - 1 or right > len(nums) - 1:
        return 
    
    mid = (left + right) // 2
    if nums[mid] == target:
        if ret[0] != -1 :
            if mid < ret[0]:
                ret[0] = mid
        else:
            ret[0] = mid
        if ret[1] != -1 :
            if mid > ret[1]:
                ret[1] = mid
        else:
            ret[1] = mid
        binarySearch(nums, target, mid+1, right, ret)
        binarySearch(nums, target, left, mid-1, ret)
    elif nums[mid] < target:
        binarySearch(nums, target, mid+1, right, ret)
    else:
        binarySearch(nums, target, left, mid-1, ret)
     

def searchRange(nums: list[int], target: int) -> list[int]:
    ret = [-1, -1]
    if len(nums) == 0:
        return ret
    if len(nums) == 1:
        if nums[0] == target:
            return [0, 0]
        else:
            return [-1, -1]
    binarySearch(nums, target, 0, len(nums)-1, ret)
    return ret


def run():
    print(searchRange([], 0))


if __name__ == "__main__":
    run()