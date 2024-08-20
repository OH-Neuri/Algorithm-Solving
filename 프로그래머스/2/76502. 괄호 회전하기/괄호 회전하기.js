
function solution(s) {
    var answer = 0;
    let list = check(s)
    const regex1 = /(\(\))/g
    const regex2 = /(\{\})/g
    const regex3 = /(\[\])/g
    for(let i = 0; i<list.length;i++){
        let num=0
        while(list[i].match(regex1)||list[i].match(regex2)||list[i].match(regex3)){

           list[i]= list[i].replace(regex1, '').replace(regex2, '').replace(regex3, '');
        }
             
        if(list[i].length===0){
            answer++
        }
    }
    return answer;
}
function check (s){
    s = s.split('')
    const list = [];
    const num = s.length;
    for(let i =0; i<num;i++){
        
    let temp = s.shift();
    s.push(temp)
    list.push(s.join(''))
    }
    return list
}