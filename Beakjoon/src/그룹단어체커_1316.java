import java.io.IOException;
import java.util.Scanner;

public class 그룹단어체커_1316 {
	static Scanner sc = new Scanner(System.in);

	public static void main(String[] args) throws IOException {
		int count = 0;
		int N = sc.nextInt();
		for (int i = 0; i < N; i++) {
			if (check() == true) {
				count++;
			}
		}
		System.out.println(count);
	}

	public static boolean check() {
		boolean[] check = new boolean[26];
		int prev = 0;
		String string = sc.next();
		for (int i = 0; i < string.length(); i++) {
			int now = string.charAt(i);

			if (prev != now) {
				if (check[now - 'a'] == false) {
					check[now - 'a'] = true;
					prev = now;
				} else {
					return false;
				}
			} else {
				continue;
			}
		}
		return true;
	}

}
