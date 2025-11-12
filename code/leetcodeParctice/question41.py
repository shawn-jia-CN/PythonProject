"""
41. 缺失的第一个正数
给你一个未排序的整数数组 nums ，请你找出其中没有出现的最小的正整数。
请你实现时间复杂度为 O(n) 并且只使用常数级别额外空间的解决方案。
"""

def firstMissingPositive(nums: list[int]) -> int:
    N = len(nums)
    for index in range(N):
        while(nums[index] <= N and nums[index] >= 1):
            to = nums[index] -1
            if nums[to] == nums[index]:
                break
            tmp = nums[to]
            nums[to] = nums[index]
            nums[index] = tmp
    print(nums)
    for index in range(N):
        if nums[index] != index + 1:
            return index + 1
    return N + 1
def run():
    print(firstMissingPositive([3,4,-1,1]))


if __name__ == "__main__":
    run()