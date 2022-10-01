import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.PriorityQueue;
import java.util.Scanner;

public class Main {
	static class Node implements Comparable<Node> {
		int v, weight;

		public Node(int v, int weight) {
			this.v = v;
			this.weight = weight;
		}

		@Override
		public int compareTo(Node o) {
			return Integer.compare(this.weight, o.weight);
		}
	}

	static final int INF = Integer.MAX_VALUE;
	static int V, E; // V : 정점 , E : 간선
	static List<Node>[] List; // 인접리스트
	static int[] dist; // 최단 길이를 저장할 값들

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		V = sc.nextInt(); // 0번부터 시작
		E = sc.nextInt();

		List = new ArrayList[V + 1];
		for (int i = 0; i < V + 1; i++)
			List[i] = new ArrayList<>();

		dist = new int[V + 1];
		Arrays.fill(dist, INF);

		for (int i = 0; i < E; i++) {
			int st = sc.nextInt();
			int ed = sc.nextInt();
			int w = sc.nextInt();

			List[st].add(new Node(ed, w)); // 인접 리스트에 넣기
			List[ed].add(new Node(st, w)); // 인접 리스트에 넣기
		}

		int v1 = sc.nextInt();
		int v2 = sc.nextInt();

		long v1Path = dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, V);
		long v2Path = dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, V);
		
		long ans= Math.min(v1Path, v2Path);
		if (ans >= INF) {
			System.out.println("-1");
		} else
			System.out.println(ans);
	}

	private static long dijkstra(int st, int ed) {
		PriorityQueue<Node> pq = new PriorityQueue<>();
		boolean[] visited = new boolean[V + 1];
		Arrays.fill(dist, INF);
		pq.add(new Node(st, 0));
		dist[st] = 0;

		while (!pq.isEmpty()) {
			Node curr = pq.poll();
			// 방문한 노드면 돌아가
			if (visited[curr.v])
				continue;
			// 처음이시군요 방문체크하고 들어가세요
			visited[curr.v] = true;
			// 현재 노드의 자식들과의 거리를 넣는다.
			for (Node node : List[curr.v]) {
				if (!visited[node.v] && dist[node.v] > dist[curr.v] + node.weight) {
					dist[node.v] = dist[curr.v] + node.weight;
					pq.add(new Node(node.v, dist[node.v]));
				}
			}
		}
		return dist[ed];
	}
}