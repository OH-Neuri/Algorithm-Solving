import java.util.*;

public class Main {
	static ArrayList<ArrayList<Integer>> graph=new ArrayList<ArrayList<Integer>>();
	static int n,m,k,x;
	static int[] d=new int[300001]; // 최단거리 저장 배열
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc=new Scanner(System.in);
		
		n=sc.nextInt();
		m=sc.nextInt();
		k=sc.nextInt();
		x=sc.nextInt();
		
		// 연결리스트에 노드 추가
		for(int i=0;i<=n;i++) {
			graph.add(new ArrayList<Integer>());
			d[i]=-1; // 최단거리 -1로 초기화
		}
		
		// 간선 정보 입력 
		for(int i=0;i<m;i++) {
			int a=sc.nextInt();
			int b=sc.nextInt();
			
			graph.get(a).add(b);
		}
		
		/*
		 * BFS 알고리즘
		 *  
		 * 모든 도로의 거리가 1이기 때문에 BFS를 사용하여 
		 * 최단거리를 구할 수 있다. 
		 */
		d[x]=0; // 시작지점의 최단거리 값 0으로 초기화
		Queue<Integer> q=new LinkedList<>();
		q.offer(x);
		while(!q.isEmpty()) {
			int now=q.poll();
			
			for(int i=0;i<graph.get(now).size();i++) {
				int next=graph.get(now).get(i);
				if(d[next]==-1) {
					// 도로의 거리가 1이기 때문에 이전 최단거리에 +1한 값 저장
					d[next]=d[now]+1;
					q.offer(next);
				}
			}
		}
		
		// 최단거리가 k인 노드 찾기 
		boolean check=false;
		for(int i=1;i<=n;i++) {
			if(d[i]==k) {
				System.out.println(i);
				check=true;
			}
		}
		
		// 최단거리가 k인 노드가 없다면 -1 출력 
		if(check==false)
			System.out.println(-1);
	}

}