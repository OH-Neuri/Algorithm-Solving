import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
	static int[] num;
	static boolean[] check;
	static StringBuilder sb = new StringBuilder();
	static int[] arr;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		num = new int[9];
		arr = new int[7];
		check = new boolean[9];
		for (int i = 0; i < 9; i++) {
			num[i] = Integer.parseInt(br.readLine());
		}
		Arrays.sort(num);
		check(0, 0);
		System.out.println();
		for(int x: arr) {
			System.out.println(x);
		}
	}
	private static void check(int idx, int sum) {
		if (sum > 100) {
			return;
		}
		int size=0;
		if (idx == 9) {
			if (sum == 100) {
				int cnt = 0;
				for (int i = 0; i < 9; i++) {
					if (check[i])
						cnt++;
				}
				if (cnt == 7) {
					for (int i = 0; i < 9; i++) {
						if (check[i])
							arr[size++]= num[i];
					}
				}
			}
			return;
		}
		check[idx] = true;
		check(idx + 1, sum + num[idx]);
		check[idx] = false;
		check(idx + 1, sum);
	}
}
