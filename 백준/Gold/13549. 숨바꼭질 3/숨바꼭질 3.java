import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	static int N, K;

	static class Node {
		int num;
		int cnt;

		public Node(int num, int cnt) {
			this.num = num;
			this.cnt = cnt;
		}

	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st = new StringTokenizer(br.readLine());
		// 수빈이의 위치
		N = Integer.parseInt(st.nextToken());
		// 동생의 위치
		K = Integer.parseInt(st.nextToken());

		System.out.println(bfs());
	}

	private static int bfs() {
		Queue<Node> q = new LinkedList<>();
		boolean[] visited = new boolean[100001];
		q.offer(new Node(N, 0));
		visited[N] = true;
		boolean check = false;
		while (!q.isEmpty()) {
			Node curr = q.poll();
			visited[curr.num] = true;
			if (curr.num == K)
				return curr.cnt;
			if (curr.num * 2 <= 100000 && !visited[curr.num * 2])
				q.add(new Node(curr.num * 2, curr.cnt));
			if (curr.num - 1 >= 0 && !visited[curr.num - 1])
				q.add(new Node(curr.num - 1, curr.cnt + 1));
			if (curr.num + 1 <= 100000 && !visited[curr.num + 1])
				q.add(new Node(curr.num + 1, curr.cnt + 1));
		}
		return 0;
	}

}
