import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static void main(String args[]) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		StringTokenizer st = new StringTokenizer(br.readLine());

		int A = Integer.parseInt(st.nextToken()); // 2
		int B = Integer.parseInt(st.nextToken()); // 162
		
		int cnt = 1;
		
		//A와 B가 같아졌거나 아니면 B가 더 작아졌거나
		while (A < B) {
			if (B % 2 == 0)
				B /= 2;
			else if (B % 10 == 1)
				B /= 10;
			else
				// 연산이 아무것도 안되면 나가버린다.
				break;
			cnt++;
		}
		// A와 B가 같다면 cnt
		if (A == B)
			System.out.println(cnt);
		else
			System.out.println(-1);

	}
}
