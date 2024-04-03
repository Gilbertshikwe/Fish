def solution(A, B):
    stack = []
    
    for i in range(len(A)):
        size, direction = A[i], B[i]
        
        # If the fish is moving downstream
        if direction == 1:
            stack.append(size)
        
        # If the fish is moving upstream
        else:
            while stack and stack[-1] < size:
                stack.pop()
            if not stack:
                stack.append(size)
    
    return len(stack)

A = [4, 3, 2, 1, 5]
B = [0, 1, 0, 0, 0]
surviving_fish = solution(A, B)
print(f"Number of surviving fish: {surviving_fish}")