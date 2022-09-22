import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

import java.util.StringTokenizer;

public class Main {
	static long A, B, C, result;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st = new StringTokenizer(br.readLine());

		A = Long.parseLong(st.nextToken());
		B = Long.parseLong(st.nextToken());
		C = Long.parseLong(st.nextToken());
		result = 1;
		System.out.println(perm2(A, B, 1));
	}

	private static long perm2(long num, long B, long result) {
		if (B == 0)
			return result%C ; 
		if ((B & 1) > 0)
			result =((result%C)*(num%C))%C;
		num =(num*num)%C;
		B = B >> 1;
		return perm2(num, B, result);

	}
}
