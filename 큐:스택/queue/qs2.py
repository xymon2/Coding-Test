#https://programmers.co.kr/learn/courses/30/lessons/42587
#항상 길이가 0,1이될때를 조심하기(edge case)

def solution(priorities, location):
    count = 0

    while True:
        cur = priorities.pop(0)

        if len(priorities) != 0 and max(priorities) > cur:
            priorities.append(cur)

            if location == 0:
                location = len(priorities) - 1
            else:
                location -= 1

        else:
            count += 1
            if location == 0:
                return count
            else:
                location -= 1

    answer = count
    return answer