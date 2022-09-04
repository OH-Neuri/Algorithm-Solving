import java.io.*;
import java.util.*;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st;
		StringBuilder sb = new StringBuilder();
		int T = Integer.parseInt(br.readLine());
		float[] num = new float[T];

		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < T; i++) {
			num[i] = Integer.parseInt(st.nextToken());
		}
		Arrays.sort(num);

		for (int i = 0; i < T - 1; i++) {
			if (num[i] % 2 == 0)
				num[T - 1] += num[i] / 2;
			else
				num[T - 1] += (num[i] / 2);
		}
			System.out.println(sb.append(num[T - 1]));
	}
}
// 20일때 20.0 이 아니라 20으로
// 소수점이 있을때는 소수점까지
// 없으면 그대로 