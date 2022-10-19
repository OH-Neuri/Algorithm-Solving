
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

	public static int N, M;
	public static int[] resultArr, arr;
	public static StringBuilder sb = new StringBuilder();
	public static boolean[] visited;

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		arr = new int[N];
		resultArr = new int[M];
		visited = new boolean[N];

		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < N; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
		Arrays.sort(arr);
		dfs(N, M, 0);
		System.out.println(sb);

	}

	public static void dfs(int N, int M, int depth) {

		if (depth == M) {
			for (int val : resultArr) {
				sb.append(val).append(' ');
			}
			sb.append('\n');
			return;
		}

		for (int i = 0; i < N; i++) {
			if (!visited[i]) {
				visited[i] = true;
				resultArr[depth] = arr[i];
				dfs(N, M, depth + 1);
				visited[i] = false;
			}
		}

	}

}