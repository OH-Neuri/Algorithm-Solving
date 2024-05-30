function solution(s) {
    return !/[a-zA-Z]/.test(s) && (s.length===4||s.length===6)? true:false 
}