import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st;
		int T = Integer.parseInt(br.readLine());
		for (int tc = 1; tc <= T; tc++) {
			st = new StringTokenizer(br.readLine());
			// A 카드 저장
			int A = Integer.parseInt(st.nextToken());
			int[][] ACard = new int[4][1];
			for (int i = 0; i < A; i++) {
				int num = Integer.parseInt(st.nextToken());
				switch (num) {
				case 4:
					ACard[0][0]++;
					break;
				case 3:
					ACard[1][0]++;
				case 2:
					ACard[2][0]++;
					break;
				case 1:
					ACard[3][0]++;
				}
			}
			// B 카드 저장
			st = new StringTokenizer(br.readLine());
			int B = Integer.parseInt(st.nextToken());// 3 3 2 1
			int[][] BCard = new int[4][1];
			for (int i = 0; i < B; i++) {
				int num = Integer.parseInt(st.nextToken());
				switch (num) {
				case 4:
					BCard[0][0]++;
					break;
				case 3:
					BCard[1][0]++;
				case 2:
					BCard[2][0]++;
					break;
				case 1:
					BCard[3][0]++;
				}
			}
			String result = "A";
			while (true) {
				if (ACard[0][0] > BCard[0][0])
					break;
				else if (ACard[0][0] < BCard[0][0]) {
					result = "B";
					break;
				} else if (ACard[1][0] > BCard[1][0])
					break;
				else if (ACard[1][0] < BCard[1][0]) {
					result = "B";
					break;
				} else if (ACard[2][0] > BCard[2][0]) {
					break;
				} else if (ACard[2][0] < BCard[2][0]) {
					result = "B";
					break;
				} else if (ACard[3][0] > BCard[3][0])
					break;
				else if (ACard[3][0] < BCard[3][0]) {
					result = "B";
					break;
				} else
					result = "D";
				break;

			}
			sb.append(result).append("\n");

		}
		System.out.println(sb);
	}

}
