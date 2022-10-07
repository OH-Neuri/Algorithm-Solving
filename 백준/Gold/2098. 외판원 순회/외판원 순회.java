import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static int[][] map, dp;
	static int N;
	static int INF = 1000000000;

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st;

		N = Integer.parseInt(br.readLine());
		map = new int[N][N];
		dp = new int[N][(1 << N) - 1];

		// 도시 정보 저장하기
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < N; j++) {
				map[i][j] = Integer.parseInt(st.nextToken());
			}
		}

		System.out.println(dfs(0, 1));
		// 비트마스킹
	}

	private static int dfs(int node, int visited) {
		// 도시를 다 선택하면 그 도시에서 시작점으로 돌아갈 수 있는지 확인한다.
		// 도시를 다 선택했으면,
		if (visited == (1 << N) - 1) {
			// 시작점으로 돌아갈 수 없으면 INF 리턴
			if (map[node][0] == 0)
				return INF;
			return map[node][0];
		}
		// 이미 아래에서 계산해서 저장된 값이 있다면 그 값을 사용하자~
		if (dp[node][visited] != 0)
			return dp[node][visited];

		int min = INF;

		for (int i = 0; i < N; i++) {
			// 아직 가보지 않았고, 시작점으로 돌아오는게 아니라면 다음 도시로 넘어가보자 ~
			if ((visited & (1 << i)) == 0 && map[node][i] != 0) {
				min = Math.min(min, dfs(i, visited | (1 << i)) + map[node][i]);
			}
		}

		dp[node][visited] = min;
		return dp[node][visited];

	}

}
