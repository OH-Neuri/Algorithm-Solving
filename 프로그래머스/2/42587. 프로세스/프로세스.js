function solution(priorities, location) {
    const queue = []
    priorities = priorities.map((priority, index) => [priority, index])
    
    while(priorities.length) {
        const [priority, index] = priorities.shift()
        const higherImportance = priorities.findIndex(([value, _]) => value > priority)
        
        if(higherImportance === -1){
            if(index === location) return queue.length + 1  
            queue.push([priority, index])  
            continue
        }
        
        priorities.push([priority, index])
    }
}