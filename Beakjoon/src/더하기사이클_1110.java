import java.util.Scanner;

public class 더하기사이클_1110 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int N = sc.nextInt();
		int num = N;
		int cnt = 0;

		do {
			cnt++;
			num = ((num % 10) * 10) + ((num / 10) + (num % 10));
	
		} while (num != N);

		System.out.println(cnt);

	}
}
