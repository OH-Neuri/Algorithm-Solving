function solution(storey) {
  if (storey < 5) return storey;
  const r = storey % 10;
  const m = (storey - r) / 10;
  return Math.min(r + solution(m), 10 - r + solution(m + 1)); 
}