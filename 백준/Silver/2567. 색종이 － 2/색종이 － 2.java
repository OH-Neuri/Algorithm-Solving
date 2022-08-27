import java.util.Scanner;

public class Main {
		static int n;
		static int[][] map;
		static int[] xpos= {0,0,1,-1};
		static int[] ypos= {1,-1,0,0};
		public static void main(String[] args) {
			Scanner sc=new Scanner(System.in);
			
			n=sc.nextInt();
			map=new int[102][102];
			for (int k = 0; k < n; k++) {
				int c=sc.nextInt();
				int r=sc.nextInt();
				for (int i = r+1; i <= r+10; i++) {
					for (int j = c+1; j <= c+10; j++) {
						map[i][j]=1;
					}
				}
			}
			
			
			int cnt=0;
			for (int i = 0; i < 102; i++) {
				for (int j = 0; j < 102; j++) {
					if(map[i][j]==1) {
						for (int k = 0; k < 4; k++) {
							int y=i+ypos[k];
							int x=j+xpos[k];
							if(x<0 || y<0 || x>=102 || y>=102)continue;
							if(map[y][x]==0) {
								cnt+=1;
							}
						}
					}
				}
			}
			System.out.println(cnt);
		}
}