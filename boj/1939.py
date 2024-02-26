def getInput():
    N, M = map(int, input().split())
    return N, M

def makeGrapgh(n: int, m: int) -> list:
    graph: list = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b,c))
        graph[b].append((a,c))
    return graph

def getSrcDest() -> tuple:
    src, dest = map(int, input().split())
    return src, dest

def check(graph: list, src: int, dest: int, mid: int) -> bool:
    visited: list = [False]*(len(graph)+1)
    visited[src] = True
    queue: list = [src]

    while queue:
        cur: int = queue.pop(0)
        for nxt, cost in graph[cur]:
            if not visited[nxt] and cost >= mid:
                visited[nxt] = True
                queue.append(nxt)
    return visited[dest]

def solution(graph: list, src: int, dest: int) -> int:
    answer: int = 0
    left: int = 1
    right: int = 1000000000

    while left <= right:
        mid: int = (left+right)//2
        if check(graph, src, dest, mid):
            answer = mid
            left = mid+1
        else:
            right = mid-1
    return answer

if __name__ == '__main__':
    n, m = getInput()
    graph = makeGrapgh(n, m)
    src, dest = getSrcDest()
    print(solution(graph, src, dest))