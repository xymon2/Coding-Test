#map
nl = list(map(int, number))

# startswith, endswith
b.startswith(a)

#문자열
ord, chr

new_id = new_id.lower()
new_id = re.sub('[^a-z0-9-_.]', '', new_id)
# new_id = re.sub('((\.)\\2{1,})', '.', new_id)
new_id = re.sub('[.]+', '.', new_id)
new_id = new_id.lstrip('.')
new_id = new_id.rstrip('.')

arr1 = re.findall("[0-9]+", dartResult)
arr2 = re.findall("[^0-9]+", dartResult)
result = re.split('([0-9]+)', dartResult)

#/D 숫자 아닌것,
result = re.split('(\D)', expression)
result = re.split('},', s)

#소수
def is_prime_number(x):
    if n<2:
        return False
    for i in range(2, x):
        if x % i == 0:
    	    return False
    return True

#정렬
b = sorted(answer.items(), key=lambda x: x[1],reverse=True)
let.sort(key = lambda x:(x.split()[1:],x.split()[0]))
answer = sorted(strings, key=lambda x: x[n])

#n진법
st = ''
while n > 0:
    d, m = divmod(n, 3)
    n = d
    st += str(m)
st = st[::-1]

#숫자인지,영어인지
s.isdigit()
s.isalpha()

#내적
from itertools import product
def solution(numbers, target):
    l = [(x, -x) for x in numbers]
    s = list(map(sum, product(*l)))
    return s.count(target)

#Counter, mostcommon
count = Counter(new_pgph)
return count.most_common(1)[0][0]

#dict
from collections import defaultdict
defaultdict(list)

#deque
from collections import deque

\
#순열조합
from itertools import permutations
b = list(permutations(a, 3))

#unpacking
# * - 튜플 언패킹 f
# ** - 딕셔너리 언패킹

#max(names, key= lambda n: len(n))

#issubset
