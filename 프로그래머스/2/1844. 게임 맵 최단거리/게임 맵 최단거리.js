function solution(maps) {
    if(maps===[1]){return 1;}
    var visit = [];
    var queue = [[0,0]];
    var moveX = [-1,1,0,0];
    var moveY = [0,0,-1,1];
    var count =1;
    if(maps[maps.length - 1][maps[0].length - 2] === 0 && maps[maps.length - 2][maps[0].length - 1] === 0) return -1;
    while(queue.length>0){
        var queLen = queue.length;
        for(var q = 0; q<queLen;q++){
            let [x,y] = queue.shift();
            for(var i =0;i<4;i++){
                var newX = x + moveX[i];
                var newY = y + moveY[i];
                if(newX===maps[0].length-1&&newY===maps.length-1) return ++count;
                if(newX>=0&&newY>=0&&newX<maps[0].length&&newY<maps.length&&maps[newY][newX]===1){
                    queue.push([newX,newY]);
                    maps[newY][newX] = 0;
                }
            }
        }
        count++;
    }
    
    return -1;
}