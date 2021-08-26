#https://programmers.co.kr/learn/courses/30/lessons/67257
#정규ㅠ표현식몰랐으면 틀렸다.
#정규표현식공부를 어떻게해야하지..?\
#카카오에 정규표현식이 자주 나오는 것 같다.

from itertools import permutations
from collections import deque
import re


def cal(n1, n2, op):
    if op == '*':
        return str(int(n1) * int(n2))
    elif op == '+':
        return str(int(n1) + int(n2))
    else:
        return str(int(n1) - int(n2))


def solution(expression):
    answer = 0
    a = ['*', '-', '+']
    b = list(permutations(a, 3))
    result = re.split('(\D)', expression)
    res = []
    for ops in b:

        t = deque(result[:])
        nt = []
        while t:
            d = t.popleft()
            if d == ops[0]:
                nt.append(cal(nt.pop(), t.popleft(), ops[0]))
            else:
                nt.append(d)

        t = deque(nt[:])
        nt = []
        while t:
            d = t.popleft()
            if d == ops[1]:
                nt.append(cal(nt.pop(), t.popleft(), ops[1]))
            else:
                nt.append(d)

        t = deque(nt[:])
        nt = []
        while t:
            d = t.popleft()
            if d == ops[2]:
                nt.append(cal(nt.pop(), t.popleft(), ops[2]))
            else:
                nt.append(d)
        res.append(abs(int(nt[0])))
    return max(res)