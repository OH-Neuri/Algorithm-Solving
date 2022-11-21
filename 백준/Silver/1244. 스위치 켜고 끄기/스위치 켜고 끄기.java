import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		// 스위치의 개수
		int N = sc.nextInt();

		// 스위치 입력
		int[] swch = new int[N];
		for (int i = 0; i < N; i++) {
			swch[i] = sc.nextInt();
		}
		// 반복문 몇개
		int K = sc.nextInt();

		for (int i = 0; i < K; i++) {
			int gen = sc.nextInt();
			int num = sc.nextInt();
			int lIdx = -1;
			int rIdx = 1;
			int cnt = 0;
			// 남자일 경우
			switch (gen) { // N:8, gen:1, num:3 ,
			case 1:
				for (int j = num - 1; j < N; j += num) {
					if (swch[j] == 1)
						swch[j] = 0;
					else
						swch[j] = 1;
				}
				break;
			// 여자일 경우
			case 2:
				if (cnt++ == 0) {
					if (swch[num - 1] == 1)
						swch[num - 1] = 0;
					else
						swch[num - 1] = 1;
				}
				while ((num - 1) + rIdx < N && (num - 1) + lIdx >= 0
						&& swch[(num - 1) + lIdx] == swch[(num - 1) + rIdx]) {
					if (swch[(num - 1) + lIdx] == 1) {
						swch[(num - 1) + lIdx] = 0;
						swch[(num - 1) + rIdx] = 0;
					} else {
						swch[(num - 1) + lIdx] = 1;
						swch[(num - 1) + rIdx] = 1;
					}
					lIdx--;
					rIdx++;
				}
			}

		}
		for (int i = 0; i < N; i++) {
			if (i == swch.length)
				break;
			if (i != 0 && i % 20 == 0)
				System.out.println();
			System.out.print(swch[i] + " ");
		}
		// 스위치상태 출력
	}

}
