"""
80. 删除有序数组中的重复项 II
给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使得出现次数超过两次的元素只出现两次 ，返回删除后数组的新长度。
不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。
"""

def removeDuplicates(nums: list[int]) -> int:
    if len(nums) <= 2:
        return len(nums)
    ans = 0
    slow = 2
    fast = 2
    while fast < len(nums):
        if nums[slow - 2] != nums[fast]:
            nums[slow] = nums[fast]
            slow = slow + 1
        fast = fast + 1
    return slow

def run():
    nums = [1,1,1,2,2,3]
    removeDuplicates(nums)
    print(nums)


if __name__ == "__main__":
    run()



    