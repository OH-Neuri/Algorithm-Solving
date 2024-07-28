function solution(s){
    let stack = []
    for(t of s){
        if(!stack || t == "("){
            stack.push(t)
        }else{
            if(stack[stack.length-1]=="("){
                stack.pop()
            }else{
                stack.push(t)
            }
        }
    }

    return stack.length==0?true:false;
}