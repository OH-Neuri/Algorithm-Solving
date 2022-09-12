import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		StringBuilder sb = new StringBuilder();
		
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		
		// 배열 채우기
		int[][] A = new int[N+1][N+1];
		for(int i=1;i<=N;i++) {
			st = new StringTokenizer(br.readLine());
			for(int j=1;j<=N;j++) {
				A[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		
		// 구간합 구하기 전에 배열에 누적합 저장하기
		// 누적합을 구하기 위해서 그 칸의 값과 왼쪽값, 위쪽값을 더해준다.(공통되는 부분은 빼준다)
		int D[][] = new int[N+1][N+1];
		for(int i =1;i<=N;i++) {
			for(int j=1;j<=N;j++) {
				D[i][j] =D[i][j-1]+ D[i-1][j] - D[i-1][j-1] + A[i][j];
			}
		}
		
		
		
		for(int i=0; i<M;i++) {
			st = new StringTokenizer(br.readLine());
			int x1 = Integer.parseInt(st.nextToken());
			int y1 = Integer.parseInt(st.nextToken());
			int x2 = Integer.parseInt(st.nextToken());
			int y2 = Integer.parseInt(st.nextToken());
			
			// 필요 없는 부분을 제거한다.
			// 이 과정에서 2번 제거된 부분은 다시 더해준다.
			int result = D[x2][y2]-D[x1-1][y2]-D[x2][y1-1] + D[x1-1][y1-1];
			System.out.println(result);
			
		}
	}

}
