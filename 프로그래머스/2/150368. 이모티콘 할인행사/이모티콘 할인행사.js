function solution(users, emoticons) {
  let answer = [];
  function dfs(idx = 0, percentArr = []) {
    if (idx === emoticons.length) {
      let members = 0;
      let amounts = new Array(users.length).fill(0);
      for (let i = 0; i < users.length; i++) {
        const user = users[i];
        for (let j = 0; j < percentArr.length; j++) {
          const percent = percentArr[j];
          const emoticon = emoticons[j];
          if (percentArr[j] >= user[0]) {
            amounts[i] += emoticon - (percent / 100) * emoticon;
          }
        }
        if (amounts[i] >= user[1]) {
          amounts[i] = 0;
          members += 1;
        }
      }

      return answer.push([members, getSumOfArray(amounts)]);
    }

    for (let i = 1; i <= 4; i++) {
      const percent = i * 10;
      percentArr.push(percent);
      dfs(idx + 1, percentArr);
      percentArr.pop();
    }
  }
  dfs();
  return answer.sort((a, b) => {
    if (a[0] > b[0]) return b[0] - a[0];
    else if (a[0] === b[0]) return b[1] - a[1];
  })[0];
}
function getSumOfArray(arr) {
  let sum = 0;
  arr.forEach((item) => {
    sum += item;
  });
  return sum;
}