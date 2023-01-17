# 스위치 켜고 끄기

def change(a): # 0, 1로 바꾸는 함수
  return 0 if a else 1

N = int(input())
switch = list(map(int, input().split())) 
M = int(input())

for _ in range(M):
  s, n = map(int, input().split())
  switch[n-1] = change(switch[n-1]) # 일단 처음 고른 숫자 바꾸기
  
  if s == 1: # 남자일 경우
    i = 2
    while n*i <= N:
      switch[n*i-1] = change(switch[n*i-1])
      i += 1
  else:  # 여자일 경우
    i = 1
    while n - i > 0 and n + i <= N and switch[n-1+i] == switch[n-1-i]:
      switch[n-1+i] = change(switch[n-1+i])
      switch[n-1-i] = change(switch[n-1-i])
      i += 1
      
for i in range(N): # 20개씩 출력
  print(switch[i], end=' ')
  if not (i+1) % 20:
    print()