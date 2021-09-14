# def convert(n, q):
#     rev_base = ''

#     while n > 0:
#         n, mod = divmod(n, q)
#         rev_base += str(mod)

#     return rev_base[::-1] 
    
# def is_prime_num(n):
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True

# def solution(n, k):
#     answer = 0
#     trans = convert(n,k)
#     trans_list = trans.split('0')
#     for i in trans_list:
#         if i and int(i)>=2 and is_prime_num(int(i)):
#             answer += 1
#     return answer
# n = 10
# k = 10
# print(solution(n,k))

# from collections import defaultdict
# from math import ceil
# def solution(fees, records):
#     answer = []
#     dict = defaultdict(list)
#     for record in records:
#         record = record.split()
#         dict[record[1]].append(record[0])
    
#     for key, value in dict.items():
#         time = 0
#         for i in range(0, len(value), 2):
#             h_in, m_in = map(int, value[i].split(':'))
#             if i == len(value)-1:
#                 h_out, m_out = 23, 59
#             else: 
#                 h_out, m_out = map(int, value[i+1].split(':'))
#             time += (m_out-m_in)+(h_out-h_in)*60
#         print(time)
#         if time > fees[0]:
#             fee = fees[1]+ceil((time-fees[0])/fees[2])*fees[3]
#         else:
#             fee = fees[1]
#         answer.append((key,fee))
#     answer = sorted(answer, key = lambda x:int(x[0]))
#     answer = [ i[1] for i in answer]
#     return answer

# fees = [180, 5000, 10, 600]
# record = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
# print(solution(fees, record))
