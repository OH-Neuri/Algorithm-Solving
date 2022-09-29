import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

public class Solution {

	static boolean[] visited;
	static List<Integer>[] list;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st;
		for (int tc = 1; tc <= 10; tc++) {
			sb.append("#").append(tc).append(" ");

			st = new StringTokenizer(br.readLine());
			// 데이터 길이
			int N = Integer.parseInt(st.nextToken());
			// 출발 지점
			int start = Integer.parseInt(st.nextToken());

			// 리스트 초기화
			list = new ArrayList[101];
			for (int i = 1; i < 101; i++) {
				list[i] = new ArrayList<>();
			}

			// 리스트에 저장
			st = new StringTokenizer(br.readLine());
			for (int i = 0; i < (N / 2); i++) {
				int s = Integer.parseInt(st.nextToken());
				int e = Integer.parseInt(st.nextToken());
				list[s].add(e);
			}

			// 깊이 배열

			visited = new boolean[101];
			// 출발
			sb.append(BFS(start)).append("\n");
		} // tc
		System.out.println(sb);
	}// main

	private static int BFS(int idx) {
		int[] D = new int[101];
		Queue<Integer> q = new LinkedList<>();
		q.offer(idx);
		visited[idx] = true;
		while (!q.isEmpty()) {
			int curr = q.poll();
			for (int x : list[curr]) {
				if (!visited[x]) {
					D[x] = D[curr] + 1;
					q.offer(x);
					visited[x] = true;
				}
			}
		}
		int max = Integer.MIN_VALUE;
		for (int i = 0; i < 101; i++) {
			if (max < D[i])
				max = D[i];
		}
		int ans = 0;
		for (int i = 0; i < 101; i++) {
			if (max == D[i])
				ans = i;
		}
		return ans;
	}
}
