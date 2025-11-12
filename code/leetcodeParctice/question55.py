"""
55. 跳跃游戏
给你一个非负整数数组 nums ，你最初位于数组的 第一个下标 。数组中的每个元素代表你在该位置可以跳跃的最大长度。
判断你是否能够到达最后一个下标，如果可以，返回 true ；否则，返回 false 。
"""

def canJump(nums: list[int]) -> bool:
    if len(nums) <= 0:
        return False
    maxLength = 0
    step = 0    
    #print("maxLength = {} step = {} ".format(maxLength, step, ))
    while step <= maxLength:
        #print("maxLength = {} step = {} nums[step] = {}".format(maxLength, step, nums[step]))
        maxLength = max(maxLength, nums[step] + step)
        #print("maxLength = {}".format(maxLength))
        if maxLength >=  len(nums) - 1:
            return True
        step = step + 1
    return False

def run():
    print(canJump([2,3,1,1,4]))


if __name__ == "__main__":
    run()