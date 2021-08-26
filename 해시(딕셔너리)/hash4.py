
#https://programmers.co.kr/learn/courses/30/lessons/42579#
# 너무 복잡한데?
#edge케이스 다시 생각 잘해보기
# 같은 숫자 여러개일때를 생각해보자.
#dict.get을 쓰면 더 낫다.

def solution(genres, plays):
    answer = []
    cnt = {}
    for i in range(len(genres)):
        if genres[i] in cnt.keys():

            cnt[genres[i]][0] += plays[i]

            if plays[i] in cnt[genres[i]][1].keys():
                cnt[genres[i]][1][plays[i]].append(i)
            else:
                cnt[genres[i]][1][plays[i]] = []
                cnt[genres[i]][1][plays[i]].append(i)
        else:
            cnt[genres[i]] = []
            cnt[genres[i]].append(plays[i])
            cnt[genres[i]].append({})

            if plays[i] in cnt[genres[i]][1].keys():
                cnt[genres[i]][1][plays[i]].append(i)
            else:
                cnt[genres[i]][1][plays[i]] = []
                cnt[genres[i]][1][plays[i]].append(i)

    a = sorted(cnt.items(), key=lambda x: x[1], reverse=True)
    # print(a)

    for key, value in a:
        b = sorted(value[1].items(), reverse=True)

        if len(b[0][1]) > 1:
            answer.append(b[0][1][0])
            answer.append(b[0][1][1])
        else:
            for i in range(2):
                answer.append(b[i][1][0])
                if len(b) == 1:
                    break
    # print(answer)

    return answer