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
		int[] in_degree = new int[N + 1];
		List<Integer>[] list = new ArrayList[N + 1];
		for (int i = 0; i <= N; i++)
			list[i] = new ArrayList<>();

		for (int i = 0; i < M; i++) {
			st = new StringTokenizer(br.readLine());
			int s = Integer.parseInt(st.nextToken());
			int e = Integer.parseInt(st.nextToken());
			list[s].add(e);
			in_degree[e]++;
		}
		int cnt = 0;
		Queue<Integer> q = new LinkedList<>();
		for (int i = 1; i <= N; i++) {
			if (in_degree[i] == 0)
				q.add(i);
		}
		while (!q.isEmpty() ) {
			int curr = q.poll();
			sb.append(curr).append(" ");
			for (int next : list[curr]) {
				if (--in_degree[next] == 0)
					q.add(next);
			}
		}
		System.out.println(sb);
	}

}
