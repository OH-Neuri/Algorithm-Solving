function solution(priorities, location) {
  let answer = 0;
  // process와 index값 저장
  const array = priorities.map((process,index) => {
    return {process, index};
  })

  while(array.length){
    const queue = array.shift();
    // some 메서드를 사용해서 queue.process 값보다 큰게 있는지 없는지 확인 있으면 push
    if(array.some((element) => element.process > queue.process)){
      array.push(queue);
    }else{
      // 없으면 answer++ index값이 location이랑 같아지면 break
      answer++
      if(queue.index === location) break;
    }
  }
  return answer;
}