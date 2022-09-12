import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		StringBuilder sb = new StringBuilder();
		int T = Integer.parseInt(br.readLine());

		// dp이용해보기
		int[][] arr = new int[T + 1][T + 1];
		int max = 0;
		for (int i = 1; i <= T; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < i; j++) {
				arr[i][j] = Integer.parseInt(st.nextToken());
				
				// 숫자 더해서 넣어보자
				if (j == 0)
					arr[i][j] += arr[i - 1][j];
				else if (i == j)
					arr[i][j] += arr[i - 1][j - 1];
				else
					arr[i][j] += Math.max(arr[i - 1][j], arr[i - 1][j - 1]);
				//바로 max값 구하기
				max = Math.max(max, arr[i][j]);
			}

		}
		System.out.println(max);

	}

}
