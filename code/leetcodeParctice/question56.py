"""
56. 合并区间
以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。请你合并所有重叠的区间，并返回 一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间 。
"""

def merge(intervals: list[list[int]]) -> list[list[int]]:
    intervals.sort(key=lambda x : x[0])
    merged = []
    for i in intervals:
        if len(merged) == 0 or i[0] > merged[-1][1]:
            merged.append(i)
        else:
            merged[-1][1] = max(merged[-1][1], i[1])
    return merged

def run():
    print(merge([[1,3],[2,6],[8,10],[15,18]]))

if __name__ == "__main__":
    run()