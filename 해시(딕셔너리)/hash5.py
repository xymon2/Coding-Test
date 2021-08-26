#https://programmers.co.kr/learn/courses/30/lessons/42888

def solution(record):
    answer = []
    db = {}
    r_answer = []
    for rec in record:
        rec = list(rec.split())
        if rec[0] == 'Enter':
            answer.append([rec[1],'님이 들어왔습니다.'])
            db[rec[1]]=rec[2]
        elif rec[0] == 'Leave':
            answer.append([rec[1],'님이 나갔습니다.'])
        else:
            db[rec[1]]=rec[2]

    for data in answer:
        db[data[0]] + data[1]
        r_answer.append(db[data[0]] + data[1])

    return r_answer