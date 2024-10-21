function solution(data, col, row_begin, row_end) {
    const sortedData = sortData(data,col-1);
    const sliceData = sortedData.slice(row_begin-1,row_end);
    
    const result = sliceData.map((tp,i)=>
        tp.reduce((ac,cur)=> (cur%(row_begin+i)) + ac ,0)
    )
    
    return result.reduce((ac,cur)=> ac ^ cur , 0);
}

function sortData(data, targetCol){
    return data.sort((a,b)=> {
        if(a[targetCol] === b[targetCol]){
            return b[0]- a[0];
        }
        return a[targetCol] - b[targetCol];
    })
    
}