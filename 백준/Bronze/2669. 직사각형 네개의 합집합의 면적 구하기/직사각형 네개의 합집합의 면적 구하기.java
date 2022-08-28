import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		int[][] arr = new int[102][102];
		for(int tc=0; tc<4;tc++) {
			st = new StringTokenizer(br.readLine());
			int x1 = Integer.parseInt(st.nextToken());
			int y1 = Integer.parseInt(st.nextToken());
			int x2 = Integer.parseInt(st.nextToken());
			int y2 = Integer.parseInt(st.nextToken());
			for(int i=x1;i<x2;i++) {
				for(int j=y1;j<y2;j++) {
					arr[i][j]=1;
				}
			}
		}//tc
		int cnt=0;
		for(int i=0;i<arr.length;i++) {
			for(int j=0;j<arr.length;j++) {
				if(arr[i][j]==1)
					cnt++;
			}
		}
		System.out.println(cnt);
		
	}

}
