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
	static List<Node>[] adjList; // 인접리스트
	static int[] dist; // 최단 길이를 저장할 값들

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		V = sc.nextInt(); // 0번부터 시작
		E = sc.nextInt();
		int start = sc.nextInt();
		
		adjList = new ArrayList[V+1];
		for (int i = 0; i < V+1; i++)
			adjList[i] = new ArrayList<>();

		dist = new int[V+1];
		Arrays.fill(dist, INF);

		for (int i = 0; i < E; i++) {
			int st = sc.nextInt();
			int ed = sc.nextInt();
			int w = sc.nextInt();

			adjList[st].add(new Node(ed, w)); // 인접 리스트에 넣기
		}

		dijkstra(start);
		for (int i = 1; i < dist.length; i++) {
			if (dist[i] == 2147483647)
				System.out.println("INF");
			else
				System.out.println(dist[i]);
		}

	}

	private static void dijkstra(int st) {
		PriorityQueue<Node> pq = new PriorityQueue<>();

		boolean[] visited = new boolean[V+1];

		pq.add(new Node(st, 0));
		dist[st] = 0;

		while (!pq.isEmpty()) {
			Node curr = pq.poll();

			if (visited[curr.v])
				continue;
			visited[curr.v] = true;

			for (Node node : adjList[curr.v]) {
				if (!visited[node.v] && dist[node.v] > dist[curr.v] + node.weight) {
					dist[node.v] = dist[curr.v] + node.weight;
					pq.add(new Node(node.v, dist[node.v]));
				}
			}
		}

	}
}