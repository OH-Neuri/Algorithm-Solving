import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

public class Solution {
	static int N, W, H, min;
	static int[][] arr, map;
	static int[] dr = { -1, 0, 1, 0 }, dc = { 0, 1, 0, -1 };

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st;
		int T = Integer.parseInt(br.readLine());
		for (int tc = 1; tc <= T; tc++) {
			st = new StringTokenizer(br.readLine());
			N = Integer.parseInt(st.nextToken());
			W = Integer.parseInt(st.nextToken());
			H = Integer.parseInt(st.nextToken());
			min = Integer.MAX_VALUE;
			arr = new int[H][W];
			for (int i = 0; i < H; i++) {
				st = new StringTokenizer(br.readLine());
				for (int j = 0; j < W; j++) {
					arr[i][j] = Integer.parseInt(st.nextToken());
				}
			}
			map = new int[H][W];
			fn_SKY(0, arr);
			sb.append("#").append(tc).append(" ").append(min).append("\n");
		} // tc
		System.out.println(sb);
	}// main

	private static void fn_SKY(int depth, int[][] arr) {
		
		check(arr);
		if (depth == N) {
			return;
		}

		map = new int[H][W];
		for (int i = 0; i < W; i++) {
//			for(int i=0; i<b.length; i++){
//	            System.arraycopy(a[i], 0, b[i], 0, a[0].length);
//	        }
			for (int k = 0; k < map.length; k++) {
				System.arraycopy(arr[k], 0, map[k], 0, arr[k].length);
			}
			for (int j = 0; j < H; j++) {
				if (map[j][i] != 0) {
					break_SKY(map[j][i], j, i);
					sort_SKY();
					fn_SKY(depth+1, map);
					break;
				}
			}
		}
	}

	private static void break_SKY(int V, int row, int col) {
		// 0 으로 만든다.
		map[row][col] = 0;
		for (int i = 0; i < 4; i++) {
			for (int j = 1; j < V; j++) {
				int nr = row + j * dr[i];
				int nc = col + j * dc[i];
				if (nr >= 0 && nr < H && nc >= 0 && nc < W && map[nr][nc] != 0) {
					break_SKY(map[nr][nc], nr, nc);
				}
			}
		}
	}

	private static void sort_SKY() {
		for (int i = 0; i < W; i++) {
			for (int j = H - 1; j >= 1; j--) {
				if (map[j][i] == 0) {
					for (int k = j-1; k >= 0; k--) {
						if (map[k][i] != 0) {
							map[j][i] = map[k][i];
							map[k][i] = 0;
							break;
						}
					}
				}
			}
		}
	}
	private static void check(int[][] map2) {
		int cnt = 0;
		for (int i = 0; i < H; i++) {
			for (int j = 0; j < W; j++) {
				if (map2[i][j] != 0)
					cnt++;
			}
		}
		if (min > cnt)
			min = cnt;
		
	}
}
