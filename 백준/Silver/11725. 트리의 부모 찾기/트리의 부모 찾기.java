
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	static ArrayList<Integer>[] nodeList;
	static boolean[] visited;
	static int[] rootNode;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		int N = Integer.parseInt(st.nextToken());

		nodeList = new ArrayList[N + 1];
		visited = new boolean[N + 1];
		rootNode = new int[N + 1];

		for (int i = 1; i < N + 1; i++) {
			nodeList[i] = new ArrayList<>();
		}

		for (int i = 0; i < N-1; i++) {
			st = new StringTokenizer(br.readLine());
			int s = Integer.parseInt(st.nextToken());
			int e = Integer.parseInt(st.nextToken());

			nodeList[s].add(e);
			nodeList[e].add(s);
		}
		for (int i = 1; i < N + 1; i++) {
			if (!visited[i]) {
				DFS(i);
			}
		}

		for (int i = 2; i < N + 1; i++) {
			System.out.println(rootNode[i]);
		}
	}

	private static void DFS(int node) {
		if (visited[node])
			return;
		visited[node] = true;
		for (int x : nodeList[node]) {
			if (visited[x]==false) {
				rootNode[x] = node;
				DFS(x);
			}
		}
	}
}
