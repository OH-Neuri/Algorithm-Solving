
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		StringBuilder sb = new StringBuilder();

		int T = Integer.parseInt(br.readLine());
		for (int tc = 1; tc <= T; tc++) {
			st = new StringTokenizer(br.readLine());
			sb.append("#").append(tc).append(" ");
			int N = Integer.parseInt(st.nextToken());
			int L = Integer.parseInt(st.nextToken());
			
			int[] ingredient = new int[N];
			int[] cal = new int[N];
			for(int i=0;i<N;i++) {
				st = new StringTokenizer(br.readLine());
				ingredient[i] = Integer.parseInt(st.nextToken());
				cal[i] = Integer.parseInt(st.nextToken());
			}
			
			int max=0;
			for (int i = 0; i < (1 << N); i++) {
				int ingreSum=0;
				int calSum=0;
				for (int j = 0; j < N; j++) {
					if ((i & 1 << j) > 0) {
						calSum +=cal[j];
						ingreSum+= ingredient[j];
					}
					if(calSum>L)
						break;
				}
				
					if(calSum<=L&& max<ingreSum)
						max=ingreSum;
			}
			sb.append(max).append("\n");
		} // tc
		System.out.println(sb);
	}// main

}
