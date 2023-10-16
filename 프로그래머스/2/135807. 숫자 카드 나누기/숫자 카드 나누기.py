def solution(arrayA, arrayB):
    answer = 0

    def gcd(a, b):
        while b > 0:
            a, b = b, a % b
        return a
    
    A = arrayA[0]
    for i in arrayA[1:]:
        A = gcd(A,i)
        
    B = arrayB[0]
    for i in arrayB[1:]:
        B = gcd(B,i)
    
    for i in arrayB:
        if i%A==0:
            A=0
            break
    for i in arrayA:
        if i%B==0:
            B=0
            break
            
    answer = max(A,B)
    return answer