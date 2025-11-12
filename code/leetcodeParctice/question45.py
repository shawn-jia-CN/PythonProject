"""
45. 跳跃游戏 II
给定一个长度为 n 的 0 索引整数数组 nums。初始位置在下标 0。
每个元素 nums[i] 表示从索引 i 向后跳转的最大长度。换句话说，如果你在索引 i 处，你可以跳转到任意 (i + j) 处：
0 <= j <= nums[i] 且
i + j < n
返回到达 n - 1 的最小跳跃次数。测试用例保证可以到达 n - 1。
实在不会了
"""
def jump(nums: list[int]) -> int:
    if len(nums) <= 0:
        return 0
    if len(nums) == 1:
        return 0
    if len(nums) == 2:
        return 1
    ans = 0
    cur_right = 0  # 已建造的桥的右端点
    next_right = 0  # 下一座桥的右端点的最大值
    for i in range(len(nums) - 1):
        # 遍历的过程中，记录下一座桥的最远点
        next_right = max(next_right, i + nums[i])
        if i == cur_right:  # 无路可走，必须建桥
            cur_right = next_right  # 建桥后，最远可以到达 next_right
            ans += 1
    return ans




    return 0

def run():
    print(jump([1,2,3]))

if __name__ == "__main__":
    run()

