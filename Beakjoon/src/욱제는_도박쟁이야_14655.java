import java.util.Scanner;

public class 욱제는_도박쟁이야_14655 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int[] fRound = new int[N];
		int[] SRound = new int[N];
		int sum = 0;
		for (int i = 0; i < N; i++) {
			fRound[i] = sc.nextInt();
		}
		for (int i = 0; i < N; i++) {
			SRound[i] = sc.nextInt();
		}
		for (int i = 0; i < N; i++) {
			if (fRound[i] > 0) {
				sum += fRound[i];
			} else {
				sum += -(fRound[i]);
			}

		}

		for (int i = 0; i < N; i++) {
			if (SRound[i] > 0) {
				sum += SRound[i];
			} else {
				sum += -SRound[i];
			}

		}
		System.out.println(sum);
	}
}
