import java.util.ArrayList;
import java.util.Scanner;

public class Main{
	static ArrayList<Integer>[] A;
	static boolean visited[];

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		// 컴퓨터의 수
		int N = sc.nextInt(); // 7
		// 컴퓨터 쌍의 수
		int K = sc.nextInt(); // 6
		//
		A = new ArrayList[N + 1];
		visited = new boolean[N + 1];

		for (int i = 1; i < N + 1; i++) {
			A[i] = new ArrayList<Integer>();
		}
		
		// 컴퓨터 쌍 저장하기
		for (int i = 0; i < K; i++) {
			int s = sc.nextInt();
			int e = sc.nextInt();
			A[s].add(e);
			A[e].add(s);
		}
		//1에서부터 DFS 실행
		DFS(1);
		
		int cnt=0;
		for(boolean f:visited) {
			if(f==true)
				cnt++;
		}
		
		//visited[0] 제외
		System.out.println(cnt-1);
		
	}//main
	static void DFS(int v) {
		if(visited[v]) 
			return;
		visited[v]=true;
		for(int i:A[v])
			if(visited[i]==false) {
				DFS(i);
			}
		
		
	}

}
