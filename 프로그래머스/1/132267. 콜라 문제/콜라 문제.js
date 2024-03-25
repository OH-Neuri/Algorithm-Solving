function solution(a, b, n) {
    
    let bottles = n
    let sum = 0
    while(bottles>=a){
        let change = Math.trunc(bottles/a)*b 
        bottles = change + bottles%a
        sum += change
    }
    return sum;
}