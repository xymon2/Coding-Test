#https://programmers.co.kr/learn/courses/30/lessons/42862
#너무 돌아간듯한느낌?

def solution(n, lost, reserve):
    answer = 0
    bstu = []
    new_lost = []
    new_reserve = []

# 같은 숫자 제거
    for stu in lost:
        if stu in reserve:
            reserve.remove(stu)
        else:
            new_lost.append(stu)

# 빌려주는 과정
    for stu in new_lost:
        if stu - 1 in reserve:
            bstu.append(stu)
            reserve.remove(stu - 1)
        elif stu + 1 in reserve:
            bstu.append(stu)
            reserve.remove(stu + 1)
        else:
            continue

# 전체 잃어버린 학생 - 빌린학생
    num = len(new_lost) - len(bstu)
    answer = n - num

    return answer