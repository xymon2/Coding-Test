#https://programmers.co.kr/learn/courses/30/lessons/81301
#re.sub랑 문자열 정규식도배우자.

import re

def solution(s):
    a = {'one':'1','two':'2','three':'3','four':'4','five':'5','six':'6',
        'seven':'7','eight':'8','nine':'9','zero':'0'}
    for k in a:
        s= re.sub(k, a[k], s)
    answer= int(s)
    return answer