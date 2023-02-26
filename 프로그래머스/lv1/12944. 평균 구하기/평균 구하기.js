function solution(arr) {
    var answer = 0;
    var sum=0;
    for(let i=0;i<arr.length;i++){
        sum += arr[i];
    }
    return answer = sum/arr.length;
}