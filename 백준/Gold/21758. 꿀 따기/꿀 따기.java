import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		int N = Integer.parseInt(br.readLine());

		int[] num = new int[100002];
		int[] ldp = new int[100002];
		int[] rdp = new int[100002];

		st = new StringTokenizer(br.readLine()); // 입력 받기
		for (int i = 1; i <= N; i++) {
			num[i] = Integer.parseInt(st.nextToken());
		}

		// 1. 벌-벌-꿀통 : 서로 양 끝쪽에 있어야 최댓값 , 끝에 있는 벌은 바로 앞자리 벌 자리 뺴줘야함
		// 2. 꿀통-벌-벌 : 서로 양 끝쪽에 있어야 최댓값, 끝에 있는 벌은 바로 뒷자리 벌 자리 뺴줘야함
		// 3. 벌-꿀통-벌 : 양쪽끝에 있는 상태에서, 꿀통의 위치를 조절해가며 양끝부터 벌꿀통 까지의 누적합이 같은 경우를 선택하면 된다.

		// 왼쪽에서 오른쪽으로 누적합 구하기
		for (int i = 1; i <= N; i++) {
			ldp[i] = ldp[i - 1] + num[i];
		}
		// 오른쪽에서 왼쪽으로 누적합 구하기
		for (int i = N; i >= 1; i--) {
			rdp[i] = rdp[i + 1] + num[i];
		}

		int answer = -1;
		
		// 벌 벌 꿀통
		// 맨 왼쪽에 벌 고정하고 벌을 오른쪽으로 이동시키면서  최댓값 구하기
		for (int i = 2; i < N; i++) {

			answer = Math.max(answer, (ldp[N] - ldp[1]) + (ldp[N] - ldp[i]) - num[i]);
		}
		// 맨 오른쪽에 벌 고정하고 벌을 왼쪽으로 이동시키면서  최댓값 구하기
		for (int i = N - 1; i >= 2; i--) {
			answer = Math.max(answer, (rdp[1]-rdp[N]) + (rdp[1] - rdp[i]) - num[i]);
		}
		// 벌 꿀통 벌
		// 
		for (int i = 2; i <= N - 1; i++) {
			int k = ldp[i];
			int o = num[i];
			answer = Math.max(answer, ldp[i]-num[1] + rdp[i]-num[N] );
		}
		System.out.println(answer);
	}
}
