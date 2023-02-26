function solution(s) {
    var answer = [];
    var arr = s.split(" ")
    for(let i=0;i<arr.length;i++){
        var first = arr[i].substr(0,1);
        var rest = arr[i].substr(1,arr[i].length-1).toLowerCase()
        if(typeof(first)=='string'){
            answer.push(first.toUpperCase() + rest)
        } else{
            answer.push(arr[i])
        }
    }
        return answer.join(" ")
}