import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static int cnt;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		int n = Integer.parseInt(st.nextToken());
		int r = Integer.parseInt(st.nextToken()); // 행
		int c = Integer.parseInt(st.nextToken()); // 열

		int size = (int) Math.pow(2, n); // 한 변의 사이즈

		cnt = 0;
		fn(size, r, c);
		System.out.println(cnt);

	}

	private static void fn(int size, int r, int c) { // 한 변이 size일때 r, c의 순서 값
		if (size == 1)
			return;

		if (r < size / 2 && c < size / 2) { // 1사분면일때
			fn(size / 2, r, c);
		}
		if (r < size / 2 && c >= size / 2) { // 2사분면일때
			cnt += (size * size) / 4;
			fn(size / 2, r, c - (size / 2));
		}
		if (r >= size / 2 && c < size / 2) { // 3사분면일때
			cnt += 2 * ((size * size) / 4);
			fn(size / 2, r - (size / 2), c);
		}
		if (r >= size / 2 && c >= size / 2) { // 4사분면일때
			cnt += 3 * ((size * size) / 4);
			fn(size / 2, r - (size / 2), c - (size / 2));
		}
	}

}
