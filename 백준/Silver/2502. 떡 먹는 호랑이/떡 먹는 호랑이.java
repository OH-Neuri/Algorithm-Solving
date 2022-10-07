import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		int D = Integer.parseInt(st.nextToken());
		int K = Integer.parseInt(st.nextToken());

		int[] arr = new int[D + 1];

		// 항상 1<=A<=B
		// A를 기준으로 B를 계속 늘려보자
		// 조건에 맞는 B가 없으면 A를 증가
		int A = 1;
		int B = 1;
		arr[1] = A;
		arr[2] = B;
		while (B < K) {
			for (int i = 3; i <= D; i++) {
				arr[i] = arr[i - 1] + arr[i - 2];
			}
			if (arr[D] == K)
				break;
			B++;
			if (B >= K) {
				A++;
				B = 1;
			}
			arr[1] = A;
			arr[2] = B;
		}
		System.out.println(arr[1]);
		System.out.println(arr[2]);
	}
}
