
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st;

		int N = Integer.parseInt(br.readLine());
		int M = Integer.parseInt(br.readLine());
		int[][] dist = new int[101][101];
		final int INF = (int)1000000000;

		// dist 배열 초기화
		for (int i = 1; i < N + 1; i++) {
			for (int j = 1; j < N + 1; j++) {
				dist[i][j] = i == j ? 0 : INF;
			}
		}

		// 간선 정보 입력 받기
		for (int i = 0; i < M; i++) {
			st = new StringTokenizer(br.readLine());
			int s = Integer.parseInt(st.nextToken());
			int e = Integer.parseInt(st.nextToken());
			int v = Integer.parseInt(st.nextToken());
			dist[s][e] = Math.min(dist[s][e], v);
		}

		// 이것이 바로 플로이드 와샬 알고리즘 ???
		for (int k = 1; k < N + 1; k++) {
			for (int i = 1; i < N + 1; i++) {
				for (int j = 1; j < N + 1; j++) {
					dist[i][j] = Math.min(dist[i][j], dist[i][k] + dist[k][j]);
				}
			}
		}

		// dist배열은 실제 최단 경로를 담고 있다고함
		for (int i = 1; i < N + 1; i++) {
			for (int j = 1; j < N + 1; j++) {
				if (dist[i][j] == INF)
					System.out.print("0 ");
				else
					System.out.print(dist[i][j] + " ");
			}
			System.out.println();
		}
	}
}
