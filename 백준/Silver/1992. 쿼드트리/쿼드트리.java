

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static char[][] arr;
	static String retVal="";

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		int n = Integer.parseInt(st.nextToken());
		arr = new char[n][n];

		for (int i = 0; i < n; i++) {
			String str = new StringTokenizer(br.readLine()).nextToken();
			arr[i]= str.toCharArray();
		}

		// 1. 4등분할 함수
		// 2. 값이 다 동일한지 확인할 함수
		func(n, 0, 0);
		check(n, 0, 0);
		System.out.println(retVal);
	}

	private static boolean check(int size, int r, int c) {
		int num = arr[r][c];
		for (int i = r; i < r + size; i++) {
			for (int j = c; j < c + size; j++) {
				if (num != arr[i][j])
					return false;
			}
		}
		return true;
	}

	private static void func(int size, int r, int c) {
		if (size == 1) {
			retVal +=arr[r][c];
			return;
		}
		if (check(size, r, c)) {
			retVal +=arr[r][c];
			return;
		} else {
			retVal+="(";
			func(size/2,r,c);
			func(size/2,r,c+size/2);
			func(size/2,r+size/2,c);
			func(size/2,r+size/2,c+size/2);
			retVal+=")";
		}
	}
}
