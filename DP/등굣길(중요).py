#https://programmers.co.kr/learn/courses/30/lessons/42898
#BSF로도 풀리긴 하나 시간초과가 뜬다
#수학적 지식을 좀 생각해야 할듯.개씨발
#행렬의 행과 열을 헷갈리지 말자.
#진짜 씨발이다.

def solution(m, n, puddles):
    mat = [[0 for j in range(m + 1)]]

    for i in range(n):
        b = [0]
        c = [0 for j in range(m)]
        b.extend(c)
        mat.append(b)

    mat[1][1] = 1

    for j in range(1, m + 1):
        for k in range(1, n + 1):
            if k == j == 1:
                continue
            if [j, k] in puddles:
                continue
            mat[k][j] = (mat[k - 1][j] + mat[k][j - 1]) % 1000000007

    return mat[n][m]
    # start = [[1,1]]
    # s_path = 0
#     while start:

#         node = start.pop()
#         if node in puddles:
#             continue
#         if node == [m,n]:
#             s_path+=1
#             spath = s_path%1000000007
#             continue

#         if not node[0]+1>m:
#             start.append([node[0]+1,node[1]])

#         if not node[1]+1>n:
#             start.append([node[0],node[1]+1])


# return s_path