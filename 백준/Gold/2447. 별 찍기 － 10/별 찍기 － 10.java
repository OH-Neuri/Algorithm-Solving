import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	static int N;
	static String[][] str;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();

		N = Integer.parseInt(br.readLine()); // 27

		// 출력될 배열
		str = new String[N][N];

		// 배열을 " " 로 채운다
		for (int i = 0; i < N; i++) {
			Arrays.fill(str[i], " ");
		}
		
		fn(0, 0, N);
		
		for(int i=0;i<N;i++) {
			for(int j=0;j<N;j++) {
				sb.append(str[i][j]);
			}
			sb.append("\n");
		}
		System.out.println(sb);
	}

	private static void fn(int x, int y, int N) {
		// N이 1이 되면 그 좌표에 "*" 넣기
		if (N == 1) {
			str[x][y] = "*";
			return;
		}

		int M = N / 3;
		// 가운데 자리는 비워두고 사각형 모양으로 돌면서 좌표 구하기
		for (int i = 0; i < 3; i++) {
			for (int j = 0; j < 3; j++) {
				if (i == 1 && j == 1)
					continue;
				fn(x + M * i, y + M * j, M);
			}
		}

	}
}
