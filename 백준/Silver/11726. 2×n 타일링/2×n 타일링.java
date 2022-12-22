

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st = new StringTokenizer(br.readLine());

		int N = Integer.parseInt(st.nextToken());

		int[] arr = new int[1001];

		arr[1] = 1;
		arr[2] = 2;
		arr[3] = 3;
		if (N > 3) {
			for (int i = 4; i <= N; i++) {
				arr[i] = (arr[i - 1] + arr[i - 2])%10007;
			}
		}
		System.out.println(arr[N]);
	}
}
