#https://programmers.co.kr/learn/courses/30/lessons/42576#
#sort사용법을 익힘.
#edge case를 직접 만들어봤다!

#멋진풀이
# import collections
#
# def solution(participant, completion):
#     answer = collections.Counter(participant) - collections.Counter(completion)
#     return list(answer.keys())[0]

# def solution(participant, completion):
#     participant.sort()
#     completion.sort()
#     for i in range(len(completion)):
#         if participant[i] != completion[i]:
#             return participant[i]
#     return participant[len(participant)-1]
# 테스트 1 〉	통과 (34.85ms, 18MB)
# 테스트 2 〉	통과 (60.52ms, 22.1MB)
# 테스트 3 〉	통과 (75.99ms, 24.7MB)
# 테스트 4 〉	통과 (76.36ms, 26.3MB)
# 테스트 5 〉	통과 (77.93ms, 26.3MB)

def solution(participant, completion):
    participant.sort()
    completion.sort()
    answer = ''

    for i in range(len(completion)):
        a = participant.pop()
        b = completion.pop()
        if a == b:
            continue
        else:
            return a

    return participant[0]

# 	통과 (44.17ms, 18.1MB) 내가 더 느리다.. ㅅㅂ
# 테스트 2 〉	통과 (55.95ms, 22.2MB)
# 테스트 3 〉	통과 (78.49ms, 24.7MB)
# 테스트 4 〉	통과 (90.22ms, 26.3MB)
# 테스트 5 〉	통과 (102.09ms, 26.3MB)