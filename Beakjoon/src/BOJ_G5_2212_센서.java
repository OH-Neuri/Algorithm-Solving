import java.util.Arrays;
import java.util.Scanner;

public class BOJ_G5_2212_센서 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		// 센서의 개수
		int N = sc.nextInt();
		// 집중국의 개수
		int K = sc.nextInt();
		// 센서를 담을 배열
		int[] sen = new int[N];
		// 센서 간격을 담을 배열
		int[] senInv = new int[N - 1];
		// 센서 간격 배열 길이
		int senL = senInv.length;
		// 구하고자하는 최솟값
		int min = 0;

		// 1
		for (int i = 0; i < N; i++) {
			sen[i] = sc.nextInt();
		}

		Arrays.sort(sen);

		// 2 간격 배열 생성
		for (int i = 0; i < senL; i++) {
			senInv[i] = sen[i + 1] - sen[i];
		}
		
		Arrays.sort(senInv);
		
		for(int i=0;i<senL-(K-1);i++) {
			min += senInv[i];
		}
		
		System.out.println(min);
		
	}// main

}
