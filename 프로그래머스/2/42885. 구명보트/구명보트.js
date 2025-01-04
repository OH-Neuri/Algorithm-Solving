function solution(people, limit) {
    let count = 0;
    people.sort((a, b) => a - b);
    
    while (people.length) {
        if (people[0] + people.at(-1) <= limit) {
            people.shift();
            people.pop();
            count++;
        } else {
            people.pop();
            count++;
        }
    }
    return count;
}