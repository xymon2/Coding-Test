#https://programmers.co.kr/learn/courses/30/lessons/49189
#그래프의 경우 그래프 연결상태를 미리 만들어두는게 시간복잡도 줄이는데 도움이 되는 것 같다.


from collections import deque

def solution(n, edge):
    answer = 0
    queue = deque([])

    #이부분
    graph = [[] for i in range(n + 1)]
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])

    queue.append([1, 0])
    visited = {}
    while queue:
        a = queue.popleft()
        if a[0] in visited:
            continue
        visited[a[0]] = a[1]

        #그때마다 전부 for item in edge하니까 시간초과
        #이렇게 연결된 노드들만 검색하니까 통과했다.
        for g in graph[a[0]]:
            if not g in visited:
                queue.append([g, a[1] + 1])

    mx = max(visited.values())
    for v in visited.values():
        if v == mx:
            answer += 1
    return answer