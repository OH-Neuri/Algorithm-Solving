import java.util.Scanner;

public class A와B_12904 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		String S = sc.next(); // B
		String T = sc.next(); // ABBA
		String[] S1 = new String[T.length()];
		String[] T1 = new String[T.length()];
		int cnt = S.length();

		// ABBA 배열에 넣기
		for (int i = 0; i < T.length(); i++) {
			T1[i] = String.valueOf(T.charAt(i));
		}
		// B 배열에 넣기
		for (int i = 0; i < S.length(); i++) {
			S1[i] = String.valueOf(S.charAt(i));
		}
		// S1에 A 더 넣기 , null인 부분에 A넣기
		for (int i = 0; i < ++cnt; i++) {
			if (S1[i].equals(null)) {
				S1[i] = "A";
				break;
			}
		}
		// S1 문자열 뒤집고 B 추가하기 => 뒤집기에서 막힘
		
		
	//	reverse(S1);
		// S1배열과 T1배열 비교하기

	}
//	static void reverse(String[] a) {
//		for(int i=0; i<a.length/2; i++) {
//			swap(a)
//		}
//	}
//	static void swap(String[] a, int idx1, int idx2) {
//		String t = a[idx1];
		
	

}
