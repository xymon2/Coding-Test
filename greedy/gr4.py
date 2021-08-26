#https://programmers.co.kr/learn/courses/30/lessons/42885
#내힘으로만 풀었다..!

from collections import deque

def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    people = deque(people)
    boats = []

    while people:
        p = people.popleft()
        a = []
        a.append(p)
        if people and p + people[-1] <= limit:
            pop = people.pop()
            a.append(pop)

        boats.append(a)

    return len(boats)