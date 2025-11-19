"""
75. 颜色分类
给定一个包含红色、白色和蓝色、共 n 个元素的数组 nums ，原地 对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。
必须在不使用库内置的 sort 函数的情况下解决这个问题。
"""
def sortColors(nums: list[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    d = {}
    for n in nums:
        if n not in d.keys():
            d[n] = 1
        else:
            d[n] = d[n] + 1
    count = 0
    for i in range(3):
        if i in d.keys():
            for j in range(d[i]):
                nums[count] = i
                count = count + 1
    return

def run():
    nums = [2,0,2,1,1,0]
    sortColors(nums)
    print(nums)

if __name__ == "__main__":
    run()