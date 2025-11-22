"""
88. 合并两个有序数组
给你两个按 非递减顺序 排列的整数数组 nums1 和 nums2,另有两个整数 m 和 n ，分别表示 nums1 和 nums2 中的元素数目。
请你 合并 nums2 到 nums1 中，使合并后的数组同样按 非递减顺序 排列。
注意：最终，合并后数组不应由函数返回，而是存储在数组 nums1 中。为了应对这种情况,nums1 的初始长度为 m + n,其中前 m 个元素表示应合并的元素，后 n 个元素为 0 ,应忽略。nums2 的长度为 n 。
"""

def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    if len(nums2) == 0:
        return
    if len(nums1) == 0:
        for n in nums2:
            nums1.append(n)
        return
    p1 = 0
    p2 = 0
    target: list = []
    while p1 < m and p2 < n:
        if nums1[p1] < nums2[p2]:
            target.append(nums1[p1])
            p1 = p1 + 1
        else:
            target.append(nums2[p2])
            p2 = p2 + 1
    if p1 < m:
        while(p1 < len(nums1)):
            target.append(nums1[p1])
            p1 = p1 + 1

    if p2 < n:
        while(p2 < len(nums2)):
            target.append(nums2[p2])
            p2 = p2 + 1
    
    for i in range(len(nums1)):
        nums1[i] = target[i]

    return

def run():
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    print(nums1)
    merge(nums1, m, nums2, n)
    print(nums1)


if __name__ == "__main__":
    run()