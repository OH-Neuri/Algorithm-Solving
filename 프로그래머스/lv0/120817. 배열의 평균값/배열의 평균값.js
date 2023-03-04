function solution(numbers) {
    return (numbers.reduce((sum,curr,i)=>sum+curr,0))/(numbers.length);
}