function solution(sizes) {
    var M = 0
    var m = 0
    for(let i=0;i<sizes.length;i++){
        if(sizes[i][0]>sizes[i][1]){
            if(sizes[i][0]>M) M = sizes[i][0]
            if(sizes[i][1]>m) m = sizes[i][1]
        }else{
            if(sizes[i][1]>=M) M=sizes[i][1]
            if(sizes[i][0]>=m) m=sizes[i][0]
        }
    }
    return M*m
}