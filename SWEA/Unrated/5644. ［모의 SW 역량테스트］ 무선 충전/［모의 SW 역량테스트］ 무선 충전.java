import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Solution {
	static int[] APath, BPath, dc = { 0, -1, 0, 1, 0 }, dr = { 0, 0, 1, 0, -1 };
	static int A, M, ans, Anr, Anc, Bnr, Bnc;
	static int[][] BC;

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st;

		int T = Integer.parseInt(br.readLine());
		for (int tc = 1; tc <= T; tc++) {
			st = new StringTokenizer(br.readLine());
			// 총 이동시간
			M = Integer.parseInt(st.nextToken());
			// BC의 개수
			A = Integer.parseInt(st.nextToken());
			BC = new int[A][4];

			// A의 이동 경로
			st = new StringTokenizer(br.readLine());
			APath = new int[M + 1];
			for (int i = 1; i < M + 1; i++) {
				APath[i] = Integer.parseInt(st.nextToken());
			}
			// B의 이동 경로
			st = new StringTokenizer(br.readLine());
			BPath = new int[M + 1];
			for (int i = 1; i < M + 1; i++) {
				BPath[i] = Integer.parseInt(st.nextToken());
			}
			// BC의 정보 저장하기
			for (int i = 0; i < A; i++) {
				st = new StringTokenizer(br.readLine());
				// x, y, 범위, 성능
				for (int j = 0; j < 4; j++) {
					BC[i][j] = Integer.parseInt(st.nextToken());
				}
			}
			// A, B의 좌표
			Anr = 1;
			Anc = 1;
			Bnr = 10;
			Bnc = 10;
			// 최대값 변수
			ans = 0;
			// 함수 시작!!!!!!!!!
			solve(0);
			sb.append("#").append(tc).append(" ").append(ans).append("\n");
		} // tc
		System.out.println(sb);
	}// main

	private static void solve(int time) {
		
		// 재귀로 시간을 1초씩 늘어나게 넘기면서
		// 그 시간에 맞게 이동시키고 그 이동한 위치와 BC의 거리가 범위 안에 들어가면
		// A와 B의 체크 배열에 그 BC에 맞게 배열에 T를하고
		// 2중포문으로 A와 B가 T가 된 경우 값을 최적화한다.
		
		if (time == M+1) {
			return;
		}
		// A와 B 한칸씩 이동시키기
		Anr += dr[APath[time]];
		Anc += dc[APath[time]];
		Bnr += dr[BPath[time]];
		Bnc += dc[BPath[time]];

		// 이동한 위치(A, B)랑 BC의 거리 확인하기
		boolean[] ACheck = new boolean[A]; 
		boolean[] BCheck = new boolean[A];
		for (int i = 0; i < A; i++) {
			// A와 BC의 거리 구하기
			int ADist = Math.abs(BC[i][0] - Anr) + Math.abs(BC[i][1] - Anc);
			if (BC[i][2] >= ADist)
				ACheck[i] = true;
			// B 와 BC의 거리 구하기
			int BDist = Math.abs(BC[i][0] - Bnr) + Math.abs(BC[i][1] - Bnc);
			if (BC[i][2] >= BDist)
				BCheck[i] = true;
		}

		int max = 0;
		int check = 0;
		for (int i = 0; i < A; i++) {
			for (int j = 0; j < A; j++) {
				check = 0;
				// i와 j가 같을 때
				if (i == j && ACheck[i] && BCheck[i]) {
					check = BC[i][3];
					// i와 j가 다를 때
				} else {
					if (ACheck[i])
						check += BC[i][3];
					if (BCheck[j])
						check += BC[j][3];
				}
				if (max < check)
					max = check;
			}
		}
		ans += max;
		solve(time + 1);
	}
}
