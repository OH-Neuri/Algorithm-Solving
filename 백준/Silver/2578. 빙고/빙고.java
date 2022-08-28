import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static int BGcnt;
	static int[][] arr;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		// 빙고판 채우기
		arr = new int[5][5];
		for (int i = 0; i < 5; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < 5; j++) {
				arr[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		BGcnt = 0;
		int cnt=0;
		out: for (int i = 0; i < 5; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < 5; j++) {
				cnt++;
				int num = Integer.parseInt(st.nextToken());
				for (int k = 0; k < 5; k++) {
					for (int m = 0; m < 5; m++) {
						
						if (arr[k][m] == num)
							arr[k][m] = 1;
						// 빙고 체크
						rCheck();
						lCheck();
						leftCheck();
						rigthCheck();
						if (BGcnt >= 3) {
							System.out.println(cnt);
							break out;
						}

						BGcnt = 0;
					}
				}
			}
		}
	}

	private static void rCheck() {
		for (int i = 0; i < 5; i++) {
			int cnt = 0;
			for (int j = 0; j < 5; j++) {
				if (arr[i][j] == 1)
					cnt++;
			}
			if (cnt == 5)
				BGcnt++;
		}
	}

	private static void lCheck() {
		for (int i = 0; i < 5; i++) {
			int cnt = 0;
			for (int j = 0; j < 5; j++) {
				if (arr[j][i] == 1)
					cnt++;
				if (cnt == 5)
					BGcnt++;
			}
		}
	}

	private static void leftCheck() {
		int cnt = 0;
		for (int i = 0; i < 5; i++) {
			if (arr[i][i] == 1)
				cnt++;
		}
		if (cnt == 5)
			BGcnt++;

	}

	private static void rigthCheck() {
		int cnt = 0;
		for (int i = 0; i < 5; i++) {
			if (arr[i][4 - i] == 1)
				cnt++;
		}
		if (cnt == 5)
			BGcnt++;
	}

}
