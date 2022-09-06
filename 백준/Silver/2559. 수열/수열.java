import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		// 문제 조건:
		// 시나리오:
		// 도구:컨트롤 인덱스, 배열에 쓰기좋게 담기, 반복문, 자료형, 문자열확인 , 델타
		// 몇개의 연속적인 날의 온도의 합의 최댓값
		// 10(전체 날짜의 수) 2(연속적인 날짜)

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int K = Integer.parseInt(st.nextToken());

		int[] arr = new int[N]; // 날짜를 담을 배열
		st = new StringTokenizer(br.readLine());

		// 날짜 배열에 담기
		for (int i = 0; i < N; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}

		int max = Integer.MIN_VALUE;
		for (int i = 0; i < N-K+1; i++) {
			int sum = 0;
			for (int j = i; j < i + K; j++) {
				sum += arr[j];
			}
			if (max < sum)
				max = sum;
		}
		System.out.println(max);
	}//main

}
