import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

import java.util.StringTokenizer;

public class Solution {
	static int A, B, result;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st;

		for (int tc = 1; tc <= 10; tc++) {
			int test_case = Integer.parseInt(br.readLine());
			sb.append("#").append(test_case).append(" ");

			st = new StringTokenizer(br.readLine());
			A = Integer.parseInt(st.nextToken());
			B = Integer.parseInt(st.nextToken());

			result = 1;	//

			sb.append(perm(A, B, 1)).append("\n");
		} // tc
		System.out.println(sb);
	}// main

	private static int perm(int num, int B, int result) {
		if (B == 0)
			return result;
		if ((B & 1) > 0)	// 비트연산을 이용해서 B의 맨 오른쪽에 1이 있다면 result에 num을 곱해준다.
			result = result * num;
		num = (num * num);  // num을 계속 늘리다가 B에서 1이 있으면 그때의 num을 곱해준다.  
		B = B >> 1;		    // B를 한칸 오른쪽으로 옮긴다. 다음 1을 확인하기 위해 
		return perm(num, B, result);

	}
}
