import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main{

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		StringBuilder sb = new StringBuilder();
		int T = Integer.parseInt(br.readLine());
		int[][] arr = new int[T + 1][4];
		int[][] dp = new int[T + 1][4];

		for (int i = 1; i <= T; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 1; j <= 3; j++) {
				arr[i][j] = Integer.parseInt(st.nextToken());
			}
		}


		dp[1][1] = arr[1][1];
		dp[1][2] = arr[1][2];
		dp[1][3] = arr[1][3];

		for (int i = 2; i <= T; i++) {
			dp[i][1] = Math.min(dp[i - 1][2], dp[i - 1][3]) + arr[i][1];
			dp[i][2] = Math.min(dp[i - 1][1], dp[i - 1][3]) + arr[i][2];
			dp[i][3] = Math.min(dp[i - 1][1], dp[i - 1][2]) + arr[i][3];
		}

		int result = Math.min(dp[T][1], Math.min(dp[T][2], dp[T][3]));

		System.out.println(result);
	}
}
