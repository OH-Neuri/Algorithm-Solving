function solution(s) {
  const len = s.length;
  let shortenLen = len;

  for (let i = 1; i <= len / 2; i++) {
    let cnt = 1;
    let temp = s.slice(0, i);
    let shortenS = "";

    for (let j = i; j < len; j += i) {
      if (temp === s.slice(j, j + i)) cnt++;
      else {
        if (cnt === 1) shortenS += temp;
        else shortenS += cnt + temp;

        cnt = 1;
        temp = s.slice(j, j + i);
      }
    }

    if (cnt === 1) shortenS += temp;
    else shortenS += cnt + temp;

    shortenLen = Math.min(shortenLen, shortenS.length);
  }

  return shortenLen;
}