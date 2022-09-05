import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		int N = Integer.parseInt(br.readLine());
		int[] arr = new int[N + 1];
		int[] d = new int[N + 1];
		// 입력 받기
		st = new StringTokenizer(br.readLine());
		for (int i = 1; i <= N; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
		
		d[1] = 1;
		for (int i = 2; i <= N; i++) {
			d[i] = 1;
			// 내 뒤에 있는 숫자들 중에서 나보다 더 크고 
			for (int j = 0; j < i; j++) {
				if (arr[i] < arr[j] && d[i] < d[j]+1)
					d[i] = d[j] + 1;
				else if (arr[i] == arr[j])
					d[i] = d[j];
			}
		}
	       int max = 0;

	        for (int i = 1; i <= N; i++)
	            max = Math.max(d[i], max);

	        System.out.println(max);
	}
}
