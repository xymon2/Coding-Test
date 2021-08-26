#https://programmers.co.kr/learn/courses/30/lessons/64065

import re

def solution(s):
    answer = []

    result = re.split('},', s)
    a = []
    for w in result:
        w = re.split(',', w)
        aa = []
        for w2 in w:
            b = list(re.sub('[{}]', '', w2))
            st = ''
            for ch in b:
                st += ch
            aa.append(int(st))
        a.append(aa)

    a.sort(key=lambda x: len(x))

    while a:
        tup = a.pop(0)
        for num in tup:
            if not num in answer:
                answer.append(num)

    return answer