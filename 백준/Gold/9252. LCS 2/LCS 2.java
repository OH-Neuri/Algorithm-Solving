
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();

		String str1 = br.readLine();
		char[] char1 = new char[str1.length() + 1];
		char1 = str1.toCharArray();
		int m = char1.length;

		String str2 = br.readLine();
		char[] char2 = new char[str2.length() + 1];
		char2 = str2.toCharArray();
		int n = char2.length;

		int[][] dp = new int[char1.length + 1][char2.length + 1];

		int lcsLength = 0;
		for (int i = 0; i <= m; i++) {
			for (int j = 0; j <= n; j++) {
				if (i == 0 || j == 0)
					dp[i][j] = 0;
				else if (char1[i - 1] == char2[j - 1])
					dp[i][j] = dp[i - 1][j - 1] + 1;
				else {
					dp[i][j] = dp[i - 1][j] > dp[i][j - 1] ? dp[i - 1][j] : dp[i][j - 1];
				}

				lcsLength = lcsLength < dp[i][j] ? dp[i][j] : lcsLength;
			}
		}

		sb.append(lcsLength).append("\n");
		Stack<Character> stack = new Stack<>();
		// 길이

		while (dp[m][n] != 0) {
			if (dp[m][n] == dp[m][n - 1])
				n--;
			else if (dp[m][n] == dp[m - 1][n])
				m--;
			else {
				stack.push(char1[m - 1]);
				m--;
				n--;
			}
		}

		while (!stack.empty()) {
			sb.append(stack.peek());
			stack.pop();
		}

		System.out.println(sb);
	}
}
