import java.io.*;
import java.util.*;

public class Main {
	 public static void main(String[] args) throws IOException{
		 //입력값의 각 자리수를 알아내기 1:계산식으로 풀어낸다, 2. 배열에 넣어서 인덱스값으로 받아낸다
		 boolean[] isNotSelfNumber = new boolean[10001];
		 for(int i=1;i<=10000;i++) {
			 int dn = getDn(i);
			 if(dn<=10000)
				isNotSelfNumber[dn]=true;
		 }
		 for(int i=1;i<isNotSelfNumber.length;i++) {
			 if(isNotSelfNumber[i]!=true) {
				 System.out.println(i);
			 }
		 }
}
	 private static int getDn(int n) {//계산한 함수
		 int dn=n;
		 while(n>0) {
			 dn+=n%10;
			 n/=10;
		 }
		 return dn;
		 
	 }
}