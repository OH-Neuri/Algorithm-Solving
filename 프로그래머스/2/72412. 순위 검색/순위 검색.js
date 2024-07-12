const binarySearch = (arr, target) => {
  let left = 0;
  let right = arr.length - 1;
  let mid = Math.floor((left + right) / 2);
  while(left <= right) {
    if (arr[mid] === target) return mid;
    if (arr[mid] < target) left = mid + 1;
    else right = mid - 1;

    mid = Math.floor((left + right) / 2);
  }
  return mid + 1; 
}

const getInfos = (info) => {
  const infos = {}; 
  info.forEach(infoString => { 
    const arr = infoString.split(" "); 
    const score = parseInt(arr.pop()); 
    const key = arr.join("");
    if (infos[key]) infos[key].push(score)
    else infos[key] = [score];
  });
  for (const key in infos) {

    infos[key].sort((a, b) => a - b); 
  }
  return infos;
}

const getResult = (infos, query, score) => {
  const infosKey = Object.keys(infos);
  return infosKey
    .filter(key => query.every(v => key.includes(v)))
    .reduce((acc, key) => acc + infos[key].length - binarySearch(infos[key], score), 0);
}

const solution = (info, query) => {
  let answer = [];
  const infos = getInfos(info); 
  query
    .map(q => q
       .split(/ and | |-/i) 
       .filter(v => v !== "") 
    ) 
    .forEach(query => {
      const score = query.pop();
      const result = getResult(infos, query, score);
      answer.push(result) 
    })
  return answer;
}