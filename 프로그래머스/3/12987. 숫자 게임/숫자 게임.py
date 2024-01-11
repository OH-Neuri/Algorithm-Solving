def solution(A, B):
    answer = 0
    
    A = sorted(A)
    B = sorted(B)
    A_idx = 0
    B_idx = 0
    
    while B_idx != len(B):
        if A[A_idx] < B[B_idx]:
            A_idx += 1
        B_idx +=1            
    return A_idx