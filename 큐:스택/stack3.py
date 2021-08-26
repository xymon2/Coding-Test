#https://programmers.co.kr/learn/courses/30/lessons/60057

def solution(s):
    answer = 0
    aa = []
    for i in range(1, len(s) + 1):
        stack = []
        for j in range(0, len(s), i):
            a = s[j:i + j]
            # print(a)
            stack.append(a)
        aa.append(stack)

    l = 1000
    for stack in aa:
        A = ''
        while stack:
            a = stack.pop()
            cnt = 1
            while stack and stack[-1] == a:
                stack.pop()
                cnt += 1
            if cnt == 1:
                A += a
            else:
                A += a
                A += str(cnt)
        l = min(l, len(A))

    return l