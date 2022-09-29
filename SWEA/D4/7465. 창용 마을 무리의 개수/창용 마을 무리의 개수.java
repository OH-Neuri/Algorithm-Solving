import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Solution {
	static boolean[] visited;
	static List<Integer>[] list;

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st;

		int T = Integer.parseInt(br.readLine());
		for (int tc = 1; tc <= T; tc++) {
			sb.append("#").append(tc).append(" ");

			st = new StringTokenizer(br.readLine());
			int N = Integer.parseInt(st.nextToken());
			int M = Integer.parseInt(st.nextToken());

			list = new ArrayList[N + 1];
			for (int i = 1; i <= N; i++) {
				list[i] = new ArrayList<>();
			}

			for (int i = 0; i < M; i++) {
				st = new StringTokenizer(br.readLine());
				int start = Integer.parseInt(st.nextToken());
				int end = Integer.parseInt(st.nextToken());
				list[start].add(end);
				list[end].add(start);
			}
			int ans = 0;
			visited = new boolean[N + 1];
			for (int i = 1; i < N+1; i++) {
				if (!visited[i])
					ans++;
				dfs(i);
			}
			sb.append(ans).append("\n");
		} // tc
		System.out.println(sb);
	}// main

	private static void dfs(int idx) {
		// 방문했다면 통과해
		if (visited[idx]) {
			return;
		}
		// 방문체크
		visited[idx] = true;
		for (int x : list[idx]) {
			if (!visited[x])
				dfs(x);
		}
	}

}
