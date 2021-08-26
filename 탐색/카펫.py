#https://programmers.co.kr/learn/courses/30/lessons/42842
#easy


def solution(brown, yellow):
    answer = []

    for i in range(yellow):
        sero = i+ 1
        garo = yellow / sero
        if sero > garo:
            break

        num = sero * 2 + garo * 2 + 4
        if num == brown:
            answer.append(garo + 2)
            answer.append(sero + 2)

    return answer