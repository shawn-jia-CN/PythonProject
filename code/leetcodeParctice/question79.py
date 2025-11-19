"""
79. 单词搜索
给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。
单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
"""
def dfs(board: list[list[str]], used: list[list[bool]], length: int, ans: list[bool], word: str, x: int, y: int):
    #print("x = {} y = {} length = {} len(word) = {} ans = {}".format(x,y, length, len(word), ans))
    #print(used)
    if len(word) - 1 == length:
        ans.append(True)
        return
    #print("length = {} len(word) = {} len(board) = {}".format(length, len(word), len(board)))
    if x > 0 and length < len(word) - 1 and not used[x-1][y] and word[length + 1] == board[x-1][y]:
        used[x-1][y] = True
        dfs(board, used, length+1, ans, word, x-1, y)
        used[x-1][y] = False
    if x < len(board) - 1 and length < len(word) - 1 and not used[x+1][y] and word[length + 1] == board[x+1][y]:
        used[x+1][y] = True
        dfs(board, used, length+1, ans, word, x+1, y)
        used[x+1][y] = False
    if y > 0  and length < len(word) - 1 and not used[x][y-1] and word[length + 1] == board[x][y-1]:
        used[x][y-1] = True
        dfs(board, used, length+1, ans, word, x, y-1)
        used[x][y-1] = False  
    if y < len(board[0]) - 1  and length < len(word) - 1 and not used[x][y+1] and word[length + 1] == board[x][y+1]:
        used[x][y+1] = True
        dfs(board, used, length+1, ans, word, x, y+1)
        used[x][y+1] = False      
    return 

def existStart(board: list[list[str]], word: str, x, y) -> bool:
    m = len(board)
    n = len(board[0])
    used = [[False for _ in range(n)] for _ in range(m)]
    ans = []
    used[x][y] = True
    dfs(board, used, 0, ans, word, x, y)
    return len(ans) > 0

def exist(board: list[list[str]], word: str) -> bool:
    m = len(board)
    n = len(board[0])
    for i in range(m):
        for j in range(n):
            if board[i][j] == word[0]:
                if existStart(board, word, i, j):
                    return True
    return False

def run():
    board = [['A','B','C','E'],['S','F','C','S'],['A','D','E','E']]
    word = "ABCCED"
   # board = [['A','B','C','E'],['S','F','C','S'],['A','D','E','E']]
   # word = "SEE"
    #board = [['A','B','C','E'],['S','F','C','S'],['A','D','E','E']]
    #word = "ABCB"

    #board = [["a","a"]]
    #word = "aaa"
    #board  = [["a","a","a","a"],["a","a","a","a"],["a","a","a","a"]]
    #word = "aaaaaaaaaaaa"
    print(exist(board, word))

if __name__ == "__main__":
    run()
