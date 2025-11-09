"""
27. 移除元素
给你一个数组 nums 和一个值 val,你需要 原地 移除所有数值等于 val 的元素。元素的顺序可能发生改变。然后返回 nums 中与 val 不同的元素的数量。
假设 nums 中不等于 val 的元素数量为 k,要通过此题，您需要执行以下操作：
更改 nums 数组，使 nums 的前 k 个元素包含不等于 val 的元素。nums 的其余元素和 nums 的大小并不重要。
"""

def removeElement(nums: list[int], val: int) -> int:
    length = 0
    left = 0
    right = 0
    if len(nums) > 0:
        while right < len(nums) :
            print("left = {} right = {}".format(left, right))
            if nums[right] != val:
                nums[left] = nums[right]
                left = left + 1
            right = right + 1
    return left

def run():
    print(removeElement([3,2,2,3], 2))

if __name__ == "__main__":
    run()