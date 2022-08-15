import java.util.Arrays;
import java.util.Comparator;
import java.util.Scanner;

public class BOJ_S1_1931_회의실배정 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		// 회의의 수
		int N = sc.nextInt();
		// 가능한 회의 개수 카운트 변수
		int cnt = 0;
		// 회의의 정보 입력받기
		int[][] num = new int[N][2];
		for (int i = 0; i < N; i++) {
			num[i][0] = sc.nextInt();
			num[i][1] = sc.nextInt();
		}

		Arrays.sort(num, new Comparator<int[]>() {
			@Override
			public int compare(int[] a, int[] b) {
				// 끝나는 시간 오름차순 정렬, 시간이 같을 경우 시작하는 시간 오름차순 정렬
				if (a[1] == b[1]) {
					return a[0] - b[0];
				} else
					return a[1] - b[1];
			}
		});
		int min = 0;
		for (int i = 0; i < N; i++) {
			if (num[i][0] >= min) {
				cnt++;
				min = num[i][1];
			}
		}
		System.out.println(cnt);
	}

}
