#https://programmers.co.kr/learn/courses/30/lessons/42860
#오랜만에 다시풀어보니 풀렸다.
#실력상승..?


def solution(name):
    answer = 0
    gname = ''
    ans = list(name)
    # ord쳐쓰지
    alp = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5,
           'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11,
           'M': 12, 'N': 13, 'O': 12, 'P': 11, 'Q': 10,
           'R': 9, 'S': 8, 'T': 7, 'U': 6, 'V': 5, 'W': 4,
           'X': 3, 'Y': 2, 'Z': 1}

    for i in range(len(name)):
        gname += 'A'

    gname = list(gname)

    if gname == ans:
        return 0

    for i in range(len(gname)):

        ch = ans[i]
        v = alp[ch]
        answer += v
        gname[i] = ch

        if gname == ans:
            return answer

        answer += 1

        part = ans[i + 1:]
        cnt = 0
        for ch in part:
            if ch != 'A':
                break
            else:
                cnt += 1

        if (cnt != 0 and cnt >= len(part) - cnt + i) or (i == 0 and cnt > 0):
            gname.reverse()
            ans.reverse()
            answer += i
            break

    for i in range(len(gname)):
        ch = ans[i]
        v = alp[ch]
        answer += v
        gname[i] = ch

        if gname == ans:
            return answer

        answer += 1