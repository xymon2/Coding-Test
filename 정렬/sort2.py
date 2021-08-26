#https://programmers.co.kr/learn/courses/30/lessons/42747#

#ㅈㄴ잘했네 휴


def solution(citations):
    answer = 0
    citations.sort()

    for idx ,value in enumerate(citations):
    #핵심. h값중 최대이므로 len으로 대체.
    #첫 값이 len보다 커야 h값 이상인 논문들 갯수이다.
        if citations[idx:][0] >= len(citations[idx:]):
            return len(citations[idx:])

    return answer