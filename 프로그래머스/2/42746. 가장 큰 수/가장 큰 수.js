function solution(numbers) {
  numbers.sort((a, b) => {
    const A = a + "";
    const B = b + "";

    const Ahead = A.charAt(0);
    const Bhead = B.charAt(0);

    if (Ahead > Bhead) return -1;
    if (Ahead === Bhead) {
      const C = +(A + B);
      const D = +(B + A);
      if (C > D) return -1;
      if (C < D) return 1;
    }
    if (Ahead < Bhead) return 1;
  });

  return Math.max(...numbers) === 0 ? "0" : numbers.join("");
}