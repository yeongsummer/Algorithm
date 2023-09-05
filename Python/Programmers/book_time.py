def solution(book_time):
    rooms = [0 for _ in range(60*24+10)]
    
    for time in book_time :
        rooms[change_minute(time[0])] += 1
        rooms[change_minute(time[1])+10] -= 1
        
    for i in range(1, len(rooms)):
        rooms[i] += rooms[i-1]
        
    return max(rooms)

def change_minute(time):
    t = time.split(':')
    return int(t[0])*60 + int(t[1])