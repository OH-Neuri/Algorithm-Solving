function solution(board) {

  function gameOver(arr,s){
    //가로 체크
    for(var y = 0;y<3;y++){
      if(arr[y][0] === s && arr[y][1] === s && arr[y][2] === s)
      {
        return true;
      }
    }

    // 세로 체크
    for(var x = 0;x<3;x++){
      if(arr[0][x] === s && arr[1][x] === s && arr[2][x] === s)
      {
        return true;
      }
    }

    //대각선 체크
    if(arr[0][0] == s && arr[1][1] == s && arr[2][2] == s){
      return true;
    }
    if(arr[0][2] == s && arr[1][1] == s && arr[2][0] ==s){
      return true;
    }

    return false;
  }


  // O,X의 개수중에 O<X면 나올수 없음
  board = board.map((element)=>{
     return element.split(""); 
  });
  
  var countO = 0;
  var countX = 0;
  for(var y =0;y<3;y++){
      for(var x = 0;x<3;x++){
          if(board[y][x] === "O"){
              countO ++;
          }
          if(board[y][x] === "X"){
              countX ++;
          }
      } 
  }
  
  //X가 더 많은 경우
  if(countO<countX){
      return 0;
  }
  
  //두 수가 같을때 O에서 이미 끝냈는지
  if(countO===countX){
    if(gameOver(board, "O")===true){
      return 0; 
    }
    else{
      return 1;
    }
  }

// O랑 X가 1개 차이 나는 경우
if(countO===countX+1){
  if(gameOver(board, "X") === false){
    return 1;
  }
}
  return 0;
  
}