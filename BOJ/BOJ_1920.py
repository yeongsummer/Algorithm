N = int(input())
n_list = list(map(int, input().split()))
n_list.sort()

M = int(input())
m_list = list(map(int, input().split()))

def binary_search(element,array,start,end):
    if start > end :
        return 0
    
    mid = (start + end) // 2

    if array[mid] == element:
        return 1
    elif array[mid] < element:
        start = mid + 1
    else:
        end = mid -1
    return binary_search(element,n_list,start,end)

for i in m_list:
    print(binary_search(i,n_list,0,N-1))