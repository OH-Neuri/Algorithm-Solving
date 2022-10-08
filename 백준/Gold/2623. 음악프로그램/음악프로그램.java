
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st = new StringTokenizer(br.readLine());

		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());

		int[] in_degree = new int[N + 1]; // 1번부터 시작
		List<Integer>[] list = new ArrayList[N + 1];
		for (int i = 1; i <= N; i++) {
			list[i] = new ArrayList<>();
		}

		for (int i = 0; i < M; i++) {
			st = new StringTokenizer(br.readLine());

			int num = Integer.parseInt(st.nextToken());
			int[] p = new int[num];

			for (int j = 0; j < num; j++) {
				p[j] = Integer.parseInt(st.nextToken());
			}

			for (int j = 0; j < num - 1; j++) {
				list[p[j]].add(p[j + 1]);
				in_degree[p[j + 1]]++;
			}
		}

		Queue<Integer> queue = new LinkedList<Integer>();
		for (int i = 1; i <= N; i++) {
			if (in_degree[i] == 0)
				queue.add(i);
		}
		int cnt = 0;
		while (!queue.isEmpty()) {
			int node = queue.poll();
			cnt++;
			sb.append(node).append("\n");
			// 해당 노드로부터 나가는 간선의 목적지의 in_degree를 1 감소
			for (int x : list[node]) {
				if (--in_degree[x] == 0)
					queue.add(x);
			}
		}
		if (cnt != N)
			System.out.println("0");
		else
			System.out.println(sb);
	}
}
