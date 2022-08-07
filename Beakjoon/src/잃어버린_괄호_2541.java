import java.util.Scanner;
import java.util.StringTokenizer;

public class 잃어버린_괄호_2541 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		// 입력값 배열에 넣기
		int sum = 0;
		int cnt = 0;
		String S = sc.next();
		for (int i = 0; i < S.length(); i++) {
			char ch = S.charAt(i);
			//+ 앞까지 계속 더하기
			//- 만나면 
		}
		StringTokenizer st = new StringTokenizer(S, "-");

		StringTokenizer sth = new StringTokenizer(st.nextToken(), "+");
		StringTokenizer sth1 = new StringTokenizer(st.nextToken(), "+");
		System.out.println(sth.nextToken());
		System.out.println(sth.nextToken());
		System.out.println(sth1.nextToken());
		System.out.println(sth1.nextToken());

	}
}
