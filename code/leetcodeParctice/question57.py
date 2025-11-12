"""
57. 插入区间
给你一个 无重叠的 ，按照区间起始端点排序的区间列表 intervals,其中 intervals[i] = [starti, endi] 表示第 i 个区间的开始和结束，并且 intervals 按照 starti 升序排列。同样给定一个区间 newInterval = [start, end] 表示另一个区间的开始和结束。
在 intervals 中插入区间 newInterval,使得 intervals 依然按照 starti 升序排列，且区间之间不重叠（如果有必要的话，可以合并区间）。
返回插入之后的 intervals。
注意 你不需要原地修改 intervals。你可以创建一个新数组然后返回它。
"""

def insert(intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
    ans = []
    need = []
    for i in intervals:
        if i[1] < newInterval[0]:
            ans.append(i)
        elif i[0] > newInterval[1]:
            ans.append(i)
        else:
            need.append(i)
    need.append(newInterval)
    megered = []
    need.sort(key=lambda x : x[0])
    for n in need:
        if len(megered) == 0 or megered[-1][1] < n[0]:
            megered.append(n)
        else:
            megered[-1][1] = max(megered[-1][1], n[1])
    ret =  ans + megered
    ret.sort(key=lambda x : x[0])
    return ret


def run():
    print(insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))

if __name__ == "__main__":
    run()