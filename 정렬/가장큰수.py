#https://programmers.co.kr/learn/courses/30/lessons/42746#

#총체적난국
# 0 일때도 생각했어야 함.
# 정렬하고 값을 조정할 경우 시간초과 발생할 확률이 높다
# idx도 건드려야하고 모든 값들을 다시 검사해야하기 때문.
# 조건을 맞춰놓고 정렬을 하도록 하자.
# 답 안봤으면 무족건틀렸을 듯

def solution(numbers):
    new_list = []
    answer = ''

    for idx, num in enumerate(numbers):
        # n1 = str(num) * 2
        # 20, 2 일때 2가먼저다 즉 1의자리를 비교
        # 위와 같은 비교가 1~1000까지이므로 1의자리 10의자리 100의자리 총 세번의 비교가 필요
        n1 = str(num) * 3
        new_list.append([n1, idx])

    new_list.sort(reverse=True)

    for item in new_list:
        answer += str(numbers[item[1]])
    # 0의 경우도 생각못했다. 반성
    if (int(answer) == 0):
        return "0"

    return answer