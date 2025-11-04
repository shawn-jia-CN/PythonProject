from collections import deque

def persion_is_seller(name: str) -> bool:
    return name[-1] == 'm'


def bfs(name: str, g: dict) -> bool:
    search_queue = deque()
    search_queue.append(name)
    history = []
    parent = {}
    path = []
    while search_queue:
        tmp = search_queue.pop()
        if tmp not in history:
            if persion_is_seller(tmp):
                p = tmp
                while p in parent.keys():
                    path.append(p)
                    p = parent[p]
                path.append(name)
                path.reverse()
                print(path)
                return True
            else:
                history.append(tmp)
                for n in g[tmp]:
                    parent[n] = tmp
                    search_queue.append(n)
    return False


def main() -> None:
    graph = {}
    graph["you"] = ["alice", "bob", "claire"]
    graph["alice"] = ["peggy"]
    graph["bob"] = ["anuj", "peggy"]
    graph["claire"] = ["thom", "jonny"]
    graph["anuj"] = []
    graph["peggy"] = []
    graph["thom"] = []
    graph["jonny"] = []   
    print(bfs("you", graph))
    return 

if __name__ == "__main__":
    main()