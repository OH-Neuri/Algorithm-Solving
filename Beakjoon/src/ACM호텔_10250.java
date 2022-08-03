import java.io.IOException;
import java.util.Scanner;
import java.io.*;
import java.util.*;

public class ACM호텔_10250 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();

		for (int i = 0; i < T; i++) {
			int H = sc.nextInt();
			int W = sc.nextInt();
			int N = sc.nextInt();
			int nCnt = 1;
			int[][] acm = new int[W][H];

			end: for (int j = 0; j < W; j++) {
				for (int k = 0; k < H; k++) {
					if (N == nCnt) {
						System.out.printf("%d%02d", k + 1, j + 1);
						break end;
					} else
						nCnt++;
				}
			}
		}
	}

}
