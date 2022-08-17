import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.Scanner;

public class BOJ_S2_1260_DFS와_BFS {
	static boolean[] visited;
	static List<Integer>[] A;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		// 정점의 개수
		int N = sc.nextInt();
		// 간선의 개수
		int M = sc.nextInt();
		// 탐색을 시작할 정점의 번호
		int V = sc.nextInt();

		A = new ArrayList[N + 1];

		for (int i = 0; i <= N; i++) {
			A[i] = new ArrayList<Integer>();
		}
		// 입력 받기
		for (int i = 0; i < M; i++) {
			int s = sc.nextInt();
			int e = sc.nextInt();
			A[s].add(e);
			A[e].add(s);
		}

		// 번호가 작은 것을 먼저 방문하기 위해 정렬하기
		for (int i = 1; i <= N; i++) {
			Collections.sort(A[i]);
		}
		// 방문 배열 초기화하기
		visited = new boolean[N + 1];
		DFS(V);
		System.out.println();
		// 방문 배열 초기화하기
		visited = new boolean[N + 1];
		BFS(V);
		System.out.println();
	}// main

	public static void DFS(int node) {
		if(visited[node])
			return;
		System.out.print(node + " ");
		visited[node] = true;
		// v의 인접한 노드들 방문 검사
		for (int x : A[node]) {
			if (!visited[x])
				DFS(x);
		}
	}

	public static void BFS(int node) {
		Queue<Integer> queue = new LinkedList<Integer>();
		// 제일 먼저 넘어온 node가 들어가고
		queue.add(node);
		visited[node] = true;

		// 큐에 남는게 없을 떄 까지
		while (!queue.isEmpty()) {
			// 방금 나간 node를 저장해서
			int now_Node = queue.poll();
			System.out.print(now_Node + " ");
			// 방금 나간 node랑 연결된 요소들의 방문여부를 확인하고
			for (int x : A[now_Node]) {
				// 만약 방문이 false 라면
				if (!visited[x]) {
					// true로 바꾸고
					visited[x] = true;
					// 연결된 요소가 큐에 들어간다
					queue.add(x);
				}
			}

		}
	}
}
