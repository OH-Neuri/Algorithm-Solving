function solution(n, wires) {
    var answer = Number.MAX_SAFE_INTEGER;
    //트리 만들기
    let tree = Array.from(Array(n+1),()=>[])
    wires.map((element)=>{
        let [a,b] = element;

        tree[a].push(b);
        tree[b].push(a);
    })
   
    function searchTree(root, exceptNum) {
        let count =0;
        let visit = [];
        let queue = [root];
        visit[root] = true;
        while(queue.length){
            let index = queue.pop();
            tree[index].forEach((element)=>{
                if(element !== exceptNum && visit[element]!==true){
                    visit[element] = true;
                    queue.push(element);
                }
            })
            count++;
        }
        
        return count;
    }

    wires.forEach(element => {
        let[a,b] = element;
        answer = Math.min(answer, Math.abs(searchTree(a,b)-searchTree(b,a)))
    });
    return answer;
}