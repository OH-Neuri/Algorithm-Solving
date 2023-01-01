

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	static boolean[] visited;
	static ArrayList<Integer>[] node;
	static StringBuilder sb;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		sb = new StringBuilder();

		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		int V = Integer.parseInt(st.nextToken());

		node = new ArrayList[N + 1];
		visited = new boolean[N + 1];

		for (int i = 1; i < N + 1; i++) {
			node[i] = new ArrayList<>();
		}

		for (int i = 0; i < M; i++) {
			st = new StringTokenizer(br.readLine());
			int s = Integer.parseInt(st.nextToken());
			int e = Integer.parseInt(st.nextToken());
			node[s].add(e);
			node[e].add(s);
		}
		for(int i=1;i<=N;i++) {
			Collections.sort(node[i]);
		}
		DFS(V);
		visited = new boolean[N + 1];
		sb.append("\n");
		BFS(V);
		System.out.println(sb);
	}

	private static void DFS(int v) {
		if (visited[v])
			return;
		visited[v] = true;
		sb.append(v).append(" ");
		for (int x : node[v]) {
			if (!visited[x]) {
				DFS(x);
			}
		}
	}

	private static void BFS(int v) {
		Queue<Integer> que = new LinkedList<>();
		que.add(v);
		visited[v] = true;
		while (!que.isEmpty()) {
			int curr = que.poll();
			sb.append(curr).append(" ");
			for (int x : node[curr]) {
				if (!visited[x]) {
					visited[x] = true;
					que.add(x);
				}
			}
		}
	}
}
