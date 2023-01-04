import java.util.Scanner;

class Main{
	static int[] num;
	static int[][] map;
	static int N;
	static int[] dx= {0,1,-1,0};
	static int[] dy= {1,0,0,-1};
	
	public static void main(String[] args){
	
		Scanner in=new Scanner(System.in);
		N=in.nextInt();
		map=new int[N][N];
		int answer=0;
		int max=0;
		int min=101;

        //입력 받기 + max,min 확인하기
		for(int i=0;i<N;i++) {
			for (int j=0;j<N;j++) {
				map[i][j]=in.nextInt();
				if(max<map[i][j]) max=map[i][j];
				if(min>map[i][j])min=map[i][j];
			}
		}
		int maxAnswer=-1;
		int cnt=min-1;

        //탐색하기
		while(true) {
			boolean[][] visit=new boolean[N][N];
			answer=0;  
			for(int i=0;i<N;i++) {
				for (int j=0;j<N;j++) {
					if(!visit[i][j] && map[i][j]>cnt) {
						dfs(i,j,visit,cnt);
						answer++;
					}
				}
		}if(maxAnswer<answer) maxAnswer=answer; cnt++;
		if(cnt>max) break;
		}
		System.out.println(maxAnswer);
		
	}
	static void dfs(int i, int j,boolean[][] visit, int cnt) {
		visit[i][j]=true;
		for(int a=0;a<4;a++) {
			int cx=i+dx[a];
			int cy=j+dy[a];
			if(cx>=0 && cx<N && cy>=0 && cy<N && !visit[cx][cy] && map[cx][cy]>cnt) {
				dfs(cx,cy,visit,cnt);
			}
		}
	}
}
