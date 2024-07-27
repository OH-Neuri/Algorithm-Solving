function solution(w, h) {
  const [n1, n2] = swap_number(w, h);
  const GCD = get_gcd(n1, n2);
  return w * h - (w + h - GCD);
}

const get_gcd = (n1, n2) => {
  if (n2 === 0) return n1;
  return get_gcd(n2, n1 % n2);
};

const swap_number = (n1, n2) => {
  if (n1 < n2) {
    [n1, n2] = [n2, n1];
  }
  return [n1, n2];
};