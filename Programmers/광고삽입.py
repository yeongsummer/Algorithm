def solution(play_time, adv_time, logs):
    answer = ''
    p_h, p_m, p_s = map(int, play_time.split(':'))

    a_h, a_m, a_s = map(int, adv_time.split(':'))
    t = 3600*a_h + 60*a_m + a_s - 1

    limit = 3600*p_h + 60*p_m + p_s

    new_logs = []
    starts = []
    ends = []
    for log in logs:
        start, end = log.split('-')
        s_h, s_m, s_s = map(int, start.split(':'))
        e_h, e_m, e_s = map(int, end.split(':'))
        start = 3600*s_h + 60*s_m + s_s
        end = 3600*e_h + 60*e_m + e_s - 1
        starts.append(start)
        ends.append(end)

    max_cnt = 0
    for start in starts:
        if t > start:
            max_cnt += 1
    
    max_cnt = 0
    while t <= limit:
        




    return answer


play_time = "02:03:55"
adv_time = "00:14:15"
logs = ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]

print(solution(play_time, adv_time, logs))