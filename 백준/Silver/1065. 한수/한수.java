import java.io.*;
import java.util.*;

public class Main {
	 public static void main(String[] args) throws IOException{
		 //입력값의 각 자리수를 알아내기 1:계산식으로 풀어낸다, 2. 배열에 넣어서 인덱스값으로 받아낸다
		Scanner sc = new Scanner(System.in);
		System.out.println(arithmetic_sequence(sc.nextInt()));
		sc.close();

	
	 }
	 public static int arithmetic_sequence(int num) {//한수 함수를 만들어서
		 int cnt =0;
		 if(num<100) {
		 return num;
		 } else {
			 cnt=99;
			 if(num==1000) {
				 num=999;//예외처리 1000보다 큰 값 넣어지면 안되니까?
			 }
			 for(int i=100;i<=num;i++) {//1~n값 사이 한수 갯수 찾기
				 int hun=i/100;
				 int ten=(i/10)%10;
				 int one=i%10;
				 
				 if((hun-ten)==(ten-one)) {
					 cnt++;
				 }
			 }
		 }
		 return cnt;
	 }
}