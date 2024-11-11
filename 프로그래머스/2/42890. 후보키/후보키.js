function solution(relation) {
  const col = relation[0].length;
  const arr = Array.from(Array(relation[0].length), (_, i) => i);
  let comb = [];
  for (let i = 0; i < col; i++) {
    comb.push(...combination(arr, i + 1));
  }

  comb = checkUnique(relation, comb);
  comb = checkMinimal(comb);
  return comb.length;
}

function combination(arr, selectNum) {
  if (selectNum === 1) return arr.map((v) => [v]);

  const result = [];
  arr.forEach((fix, i, origin) => {
    const combi = combination(origin.slice(i + 1), selectNum - 1);
    const attach = combi.map((c) => [fix, ...c]);
    result.push(...attach);
  });
  return result;
}

function checkUnique(relation, comb) {
  let result = [];

  comb.forEach((c) => {
    let set = new Set();
    relation.forEach((rel) => set.add(c.map((e) => rel[e]).join(',')));
    if (set.size == relation.length) result.push(c);
  });

  return result;
}

function checkMinimal(comb) {
  let result = [];

  while (comb.length) {
    result.push(comb[0]);
    comb = comb.reduce((a, c) => {
      if (!comb[0].every((e) => c.includes(e))) a.push(c);
      return a;
    }, []);
  }

  return result;
}