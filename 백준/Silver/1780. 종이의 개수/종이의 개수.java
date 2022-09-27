import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static int N;
	static int[] num;
	static int[][] arr;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		StringBuilder sb = new StringBuilder();

		N = Integer.parseInt(br.readLine());
		arr = new int[N][N];

		// 입력받기
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < N; j++) {
				arr[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		// 0:-1, 1:0, 2:1
		num = new int[3];
		partition(0, 0, N);
		
		for (int x : num) {
			System.out.println(x);
		}
	}
	// 1. 사각형의 값이 다 일치하는지 확인한다 -> 일치하면 값 읽어오기
	// 2. 아닐 경우 9등분한다.
	// 3. 9등분한 값을 다시 확인한다. 반복

	private static void partition(int row, int col, int size) {
		// 사각형의 값이 다 일치하는지 확인하고
		if (check(row, col, size)){
			// 값이 -1일경우
			if (arr[row][col] == -1)
				num[0]++;
			// 값이 0일경우
			else if (arr[row][col] == 0)
				num[1]++;
			// 값이 1일경우
			else
				num[2]++;

			return;
		}
		// 사각형의 값이 다 일치하지 않을 경우 9등분하자 ~
		size = size / 3;
		for (int i = 0; i < 3; i++) {
			for (int j = 0; j < 3; j++) {
				partition(row + i * size, col + j * size, size);
			}
		}
	}

	// 사각형의 값이 다 일치하는지 확인하는 함수
	private static boolean check(int row, int col, int size) {
		// 사이즈가 1일 경우
		int check = arr[row][col];
			
		for (int i = row; i < row+size; i++) {
			for (int j = col; j < col+ size; j++) {
				if (check!=arr[i][j])
					return false;
			}
		}
		return true;
	}
}
