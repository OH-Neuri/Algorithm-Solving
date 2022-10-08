
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st;

		int N = Integer.parseInt(br.readLine());
		int[] arrow = new int[10000001]; //N 크기가 1~1000000

		st = new StringTokenizer(br.readLine());
		int cnt=0;
		for (int i = 0; i < N; i++) {
			int balloon = Integer.parseInt(st.nextToken());
			// 내려오는 화살이 없다면
			if(arrow[balloon+1]==0) {
				arrow[balloon]++;
				cnt++;
			}else {
				// 내려오는 화살이 있다면! 아래로 이동시킨다.
				arrow[balloon+1]--;
				arrow[balloon]++;
			}
		}
		System.out.println(cnt);
	}
}
