# def makeTable(P):
#     lp = len(P)
#     Table = [0]*lp
#     i = 0
#     for j in range(1,lp):
#         while i > 0 and P[i] != P[j]:
#             i = Table[i-1]
#         if P[i] == P[j]:
#             i += 1
#             Table[j] = i
#     return Table

# def KMP(P,T):
#     ans = []
#     lt = len(T)
#     lp = len(P)
#     table = makeTable(P)
#     i = 0
#     for j in range(lt):
#         while i > 0 and P[i] != T[j]:
#             i = table[i-1]
#         if P[i] == T[j]:
#             if i == lp-1:
#                 ans.append(j-lp+2)
#                 i = table[i]
#             else:
#                 i += 1
#     return ans

# def solution(goods):
#     answer = []
#     for good in goods:
#         keywords = []
#         for n in range(len(good)):
#             flag = False
#             for i in range(len(good)-n):
#                 keyword = good[i:i+n+1]
#                 if keyword in keywords:
#                     continue

#                 for find_good in goods:
#                     if good != find_good and KMP(keyword, find_good):
#                         break
#                 else:
#                     keywords.append(keyword)
#                     flag = True

#             if flag:
#                 break
            
#         if keywords:
#             answer.append(' '.join(sorted(keywords)))
#         else:
#             answer.append("None")
#     return answer

# from collections import deque

# def solution(arr, processes):
#     answer = []
#     reads = [0]*1001
#     writes = [0]*1001
#     N = len(processes)

#     for process in processes:
#         query = process.split()
#         if query[0] == "read":
#             reads[int(query[1])] = list(map(int, query[2:]))
#         else:
#             writes[int(query[1])] = list(map(int, query[2:]))

#     todo_reads = deque()
#     todo_writes = deque()
#     finish_time = 0
#     inprogress = "empty"
#     n = 0
#     time = 0
#     i = 0
#     while True:
#         print(finish_time, i)
#         if finish_time == i:
#             inprogress = "empty"
        
#         if i < 1000:
#             if reads[i]:
#                 todo_reads.append(reads[i])
#             if writes[i]:
#                 todo_writes.append(writes[i])

#         print(todo_reads)
#         print(todo_writes)

#         if inprogress == "read" and not todo_writes:
#             if todo_reads:
#                 t2, n1, n2 = todo_reads.popleft()
#                 answer.append(''.join(arr[n1:n2+1]))
#                 finish_time = max(finish_time, i + t2)
#                 n += 1

#         elif inprogress == "empty":
#             if todo_writes:
#                 t2, n1, n2, new = todo_writes.popleft()
#                 for j in range(n1, n2+1):
#                     arr[j] = str(new)
#                 finish_time = i + t2
#                 inprogress = "write"
#                 n += 1
#             elif todo_reads:
#                 while todo_reads:
#                     t2, n1, n2 = todo_reads.popleft()
#                     answer.append(''.join(arr[n1:n2+1]))
#                     finish_time = max(finish_time, i + t2)
#                     n += 1
#                 inprogress = "read"
#         print(inprogress, time)

#         if i < finish_time:
#             time += 1

#         if N == n and i == finish_time:
#             break
#         i += 1

#     answer.append(str(time))
#     return answer


# arr = ["1","1","1","1","1","1","1"]
# processes = ["write 1 12 1 5 8","read 2 3 0 2","read 5 5 1 2","read 7 5 2 5","write 13 4 0 1 3","write 19 3 3 5 5","read 30 4 0 6","read 32 3 1 5"]
# print(solution(arr, processes))



def solution(n, m, k, records):
    def find(i, password):
        nonlocal n, m, pattern, l, passwords

        limit = 0
        if password:
            limit = password[-1]

        if i == l:
            passwords.append(password)
            return
        
        for j in range(limit+1, m+1):
            if m - j >= l - i - 1:
                if i >= 1 and pattern[i] - pattern[i-1] >= j - password[-1]:
                    find(i+1, password+[j])
                if i == 0:
                    find(i+1, password+[j])

    answer = []
    for record in records:
        passwords = []
        pattern = sorted(list(set(record)))
        l = len(pattern)
        
        if pattern[0] == 1:
            find(1, [1])
        else:
            find(0, [])

        if not answer:
            answer = passwords
        else:
            new_answer = []
            for ans in answer:
                if ans in passwords:
                    new_answer.append(ans)
            answer = new_answer

    answer = sorted(answer, reverse=True)[0]
    pattern = sorted(list(set(records[0])))

    password_dict = {}
    for i, j in zip(answer, pattern):
        password_dict[j] = i
    result = []
    for i in records[0]:
        result.append(password_dict[i])
        
    return result

# print(solution(8,4,4,[[1, 5, 1, 3], [5, 7, 5, 6]]))
