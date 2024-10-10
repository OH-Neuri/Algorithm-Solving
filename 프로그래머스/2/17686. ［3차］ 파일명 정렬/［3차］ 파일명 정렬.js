function solution(files) {
    var answer = [];
    let list = []
    for(const file of files){
        let head = ''
        let number = ''
        for(const f of file){
            if(!isNaN(parseInt(f)) && number.length < 6){
                number += f
            }
            else{
                if(number){
                    break
                }
                head += f
            }
        }
        list.push([head.toLowerCase(), Number(number), file])
    }
    list.sort((a, b) => {
    if(a[0] !== b[0]){
        return a[0] > b[0] ? 1 : -1
    }
    else{
        if(a[1] !== b[1]){
            return a[1] > b[1] ? 1 : -1
        }
        else{
            return files.indexOf(a[2]) > files.indexOf(b[2]) ? 1 : -1
        }
    }
    })
    for(l of list){
        answer.push(l[2])
    }
    return answer;
}