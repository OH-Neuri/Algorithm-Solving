import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {
	static int[] month, fee;
	static int min;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st;

		int T = Integer.parseInt(br.readLine());
		for (int tc = 1; tc <= T; tc++) {
			sb.append("#").append(tc).append(" ");

			st = new StringTokenizer(br.readLine());
			// 요금 배열
			fee = new int[5];
			for (int i = 1; i < fee.length; i++) {
				fee[i] = Integer.parseInt(st.nextToken());
			}

			st = new StringTokenizer(br.readLine());
			// 이용 계획
			month = new int[13];
			for (int i = 1; i < month.length; i++) {
				month[i] = Integer.parseInt(st.nextToken());
			}

			min = fee[4];
			fn(1, 0);
			sb.append(min).append("\n");
		} // tc
		System.out.println(sb);
	}// main

	private static void fn(int m, int feeSum) {
		if (min < feeSum)
			return;
		else if (m >= 13) {
			min = feeSum;
			return;
		}
		// 1일 이용권 사용
		if (month[m] * fee[1] < fee[2])
			fn(m + 1, feeSum + month[m] * fee[1]);
		else
			fn(m + 1, feeSum + fee[2]);
		// 3달 이용권 사용
		fn(m + 3, feeSum + fee[3]);
	}
}
