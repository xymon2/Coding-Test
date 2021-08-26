#https://programmers.co.kr/learn/courses/30/lessons/42586

#edge케이스 잘 생각할 것.


from collections import deque

def solution(progresses, speeds):
    progresses = deque(progresses)
    speeds = deque(speeds)

    answer = []
    while len(progresses) > 0:
        a = 0

        for i in range(len(progresses)):
            progresses[i] += speeds[i]

        #이부분 테스트케이스에없었으면 틀릴뻔
        while len(progresses) != 0 and progresses[0] > 99:
            progresses.popleft()
            speeds.popleft()
            a += 1

        if a > 0:
            answer.append(a)

        # if len(progresses) == 0:
        #     break 불필요한부분

    return answer