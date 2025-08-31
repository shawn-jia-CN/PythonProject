import sys
"""
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。
你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。
你可以按任意顺序返回答案。
"""
    
def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    data = {}
    id = 0 
    for i in nums:
        if target - i in data.keys():
            return [id, data[target-i]]
        data[i] = id
        id = id + 1
    return None

def run():
   # nums = [2,7,11,15], target = 9
    nums = [3,2,4]
    target = 6
    print("ans = {}".format(twoSum(nums, target)))
    return 

if __name__ == "__main__":
    run()
