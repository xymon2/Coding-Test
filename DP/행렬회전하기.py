# https://programmers.co.kr/learn/courses/30/lessons/77485

def solution(rows, columns, queries):
    answer = []

    mat = [[]]
    for i in range(1, rows * columns, columns):
        a = [[]]
        b = [j for j in range(i, i + columns)]
        a.extend(b)
        mat.append(a)

    for q in queries:

        mm = []

        ru = mat[q[0]][q[3]]
        ld = mat[q[2]][q[1]]
        lu = mat[q[0]][q[1]]

        for i in range(q[1] + 1, q[3] + 1):
            mm.append(mat[q[0]][i])
            tmp = mat[q[0]][i]
            mat[q[0]][i] = lu
            lu = tmp

        for i in range(q[1], q[3]):
            mm.append(mat[q[2]][i])
            mat[q[2]][i] = mat[q[2]][i + 1]

        for i in range(q[0] + 1, q[2] + 1):
            mm.append(mat[i][q[3]])
            tmp = mat[i][q[3]]
            mat[i][q[3]] = ru
            ru = tmp

        for i in range(q[0], q[2]):
            mm.append(mat[i][q[1]])
            mat[i][q[1]] = mat[i + 1][q[1]]

        mat[q[2] - 1][q[1]] = ld

        mm.append(ld)
        answer.append(min(mm))

    return answer