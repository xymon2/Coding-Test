#https://programmers.co.kr/learn/courses/30/lessons/17677#
from collections import defaultdict

def solution(str1, str2):
    str1 = str1.upper()
    str2 = str2.upper()
    st1 = defaultdict(int)
    st2 = defaultdict(int)
    st11 = set()
    st22 = set()

    for i in range(len(str1 ) -1):
        a = str1[i: i +2]
        if a[0].isalpha() and a[1].isalpha():
            st1[a ]+ =1

    for i in range(len(str2 ) -1):
        a = str2[i: i +2]
        if a[0].isalpha() and a[1].isalpha():
            st2[a ]+ =1

    for key ,value in st1.items():
        if value >1:
            for i in range(value):
                st11.add(key + str(i))
        else:
            st11.add(key + str(value))

    for key, value in st2.items():
        if value > 1:
            for i in range(value):
                st22.add(key + str(i))
        else:
            st22.add(key + str(value))

    inter = len(st11 & st22)
    union = len(st11 | st22)

    if union == 0:
        return 65536

    answer = int((inter / union) * 65536)

    return answer