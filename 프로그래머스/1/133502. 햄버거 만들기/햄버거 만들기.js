function solution(ingredient) {
    let stack = []
    let sum =0
    for(let i=0;i<ingredient.length;i++){
        stack.push(ingredient[i]);
        
        if(stack.length<4) continue
        let check = stack.slice(-4)
        if(check.join('')=='1231') {
            sum +=1
            stack.splice(-4)
        }
    }
    return sum;
}