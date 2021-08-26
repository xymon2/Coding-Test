#https://programmers.co.kr/learn/courses/30/lessons/42860
#개억지로 했음
#앞에 A갯수를 세서 오른쪽으로갈지 왼쪽으로갈지 정했어야하는데
#그런거몰라씨발
#아마 좀 철저한 테스트케이스였으면 더 틀렸을 것

def solution(name):
    answer1 = 0
    answer2 = 0
    nl = list(name)
    # ord쳐쓰지
    alp = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5,
           'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11,
           'M': 12, 'N': 13, 'O': 12, 'P': 11, 'Q': 10,
           'R': 9, 'S': 8, 'T': 7, 'U': 6, 'V': 5, 'W': 4,
           'X': 3, 'Y': 2, 'Z': 1}
    flag = 0
    for idx, ch in enumerate(name):
        if idx == 1 and ch == 'A':
            answer1 -= 1
            flag = 1
            answer1 += alp[ch]
            continue
#A가 연속된다면
        if flag == 1 and ch == 'A':
            answer1 -= 1
            continue

        answer1 += alp[ch]
        flag = 0

    answer1 += len(name) - 1

    return answer1

