function solution(s) {
    let arr = s.split(' ').map(i=>i.toLowerCase())
    let answer = ''
    for(a of arr){
      for(let i=0; i<a.length;i++){
          if(i%2==0){answer+=a[i].toUpperCase()}else{answer+=a[i]}
      }
        answer +=' '
    }
    answer = answer.slice(0,-1)
        
    return answer
}