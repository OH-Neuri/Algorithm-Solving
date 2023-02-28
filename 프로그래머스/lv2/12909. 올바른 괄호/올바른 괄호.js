function solution(s){
    var arr = (s+"").split("")
    var stackCount=0;
    for(let i=0;i<arr.length;i++){
        if(arr[i]=='(')
            stackCount++;
        else if(arr[i]==')')
            stackCount--;
        if(stackCount<0)
            return false;
    }
    return stackCount==0?true:false;
}