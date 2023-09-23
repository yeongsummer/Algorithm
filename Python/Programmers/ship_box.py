def solution(order):
    stack = []
    box = 1
    target_idx = 0
    
    while target_idx < len(order):
        if order[target_idx] == box:
            target_idx += 1
            box += 1
        elif len(stack) > 0 and order[target_idx] == stack[-1]:
            target_idx += 1
            stack.pop()
        elif box <= len(order):
            stack.append(box)
            box += 1
        else:
            break
        
    return target_idx