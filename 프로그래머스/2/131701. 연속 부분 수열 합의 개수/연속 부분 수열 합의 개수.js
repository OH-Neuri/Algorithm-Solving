function solution(elements) {
  const set = new Set(); 
  const n = elements.length; 
  
  for(let i=0; i<n; i++){
    // 합계 저장
    let sum = 0;
    for(let j=i; j<i+n; j++){
      // % 인덱스를 순환하면서 sum에 더함
      sum += elements[j%n];
      set.add(sum)
    }

  }
  return set.size
}