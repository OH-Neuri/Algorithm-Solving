import java.io.*;

class Solution {
    public int[] solution(int brown, int yellow) {
        int[] answer= new int[2];
        out :for(int i=3;i<=5000;i++){
            for(int j=3;j<=i;j++){
                if(i*j>brown+yellow)
                    break;
                if(i*j==brown+yellow){
                    int check = (i-2)*(j-2);
                    if(check==yellow){
                     answer[0]=i;
                     answer[1]=j;
                    break out;
                    }
                }
            }
        }
        
        return answer;
    }
}