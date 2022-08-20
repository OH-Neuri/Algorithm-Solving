import java.util.Scanner;

public class BOJ_S1_1052_물병 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int N = sc.nextInt(); //13
		int K = sc.nextInt(); //2


		int cnt = 0;
		if (N <= K) {
			System.out.println(0);
			return;
		}
		
		int buy = 0;
		while (true) {
			cnt = 0;
			int N2 = N;
			// N2를 2로 계속 나눠서 나머지 1 몇번 나왔는지 카운트
			while (N2 != 0) {
				if (N2 % 2 == 1) {
					cnt += 1;
				}
				N2 /= 2;
			}//cnt가 K보다 크면 물병을 하나 산다, K개로 만드는게 불가능하다는 것
			if(cnt<=K)
				break;
			N+=1;
			buy+=1;
		}
		System.out.println(buy);

}
	
}
