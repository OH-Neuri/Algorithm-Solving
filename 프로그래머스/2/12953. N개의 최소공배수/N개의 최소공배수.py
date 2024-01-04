def solution(arr):
    def GCD(x,y):
        while y:
            x,y = y,x%y
        return x
    
    def LCM(x,y):
        result = x*y//GCD(x,y)
        return result
    
    result = LCM(arr[0],arr[1])
    for i in range(2,len(arr)):
        result = LCM(result,arr[i])
    
    return result