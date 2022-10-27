class Solution {
    public int solution(int n) {
        int answer = 0;
        
        // n을 2진수로 변환
        String binaryN = Integer.toBinaryString(n);
        // n의 1의 개수를 저장
        int countOfN = countOfOne(binaryN);
        
        int num = n + 1;
        
        while(true){
            // num을 2진수로 변환 후 n과 1의 개수가 같은지 확인한다.
            if(countOfOne(Integer.toBinaryString(num))==countOfN){
                answer = num;
                break;
            }
            num++;
        }
        return answer;
    }
    // 2진수에서 1의 개수를 구하는 함수
    static int countOfOne(String binaryNum){
        int count=0;
        for(int i=0;i<binaryNum.length();i++){
            if(binaryNum.charAt(i)-'0'==1){
                count++;
            }
        }
        return count;
    }
}