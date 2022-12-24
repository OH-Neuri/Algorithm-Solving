
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static int blue, white;
	static int[][] arr;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		int n = Integer.parseInt(st.nextToken());
		arr = new int[n][n];

		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < n; j++) {
				arr[i][j] = Integer.parseInt(st.nextToken());
			}
		}

		// 4등분 함수
		func(n, 0, 0);
		// 색종이 전체 색 체크
		check(n, 0, 0);
		
		System.out.println(white+"\n"+blue);
	}

	private static void isBule(int r, int c) {
		if (arr[r][c] == 1)
			blue++;
		else
			white++;
	}

	private static boolean check(int size, int r, int c) {
		int color = arr[r][c];
		for (int i = r; i < r + size; i++) {
			for (int j = c; j < c + size; j++) {
				if (color != arr[i][j])
					return false;
			}
		}
		return true;
	}

	private static void func(int size, int r, int c) {
		// 1칸일때 끝남
		if (size == 1) {
			isBule(r, c);
			return;
		}
		// 색이 다 맞는지 체크
		if (check(size, r, c)) {
			isBule(r, c);
		} else {
			//안맞으면 4등분하기
			func(size/2,r,c);
			func(size/2,r,c+size/2);
			func(size/2,r+size/2,c);
			func(size/2,r+size/2,c+size/2);
		}
	}
}
