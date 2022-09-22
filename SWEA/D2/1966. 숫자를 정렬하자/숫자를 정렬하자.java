import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st;

		int T = Integer.parseInt(br.readLine());
		for (int tc = 1; tc <= T; tc++) {
			sb.append("#").append(tc).append(" ");

			int N = Integer.parseInt(br.readLine());
			int[] arr = new int[N];

			// N 입력받기
			st = new StringTokenizer(br.readLine());
			for (int i = 0; i < N; i++) {
				arr[i] = Integer.parseInt(st.nextToken());
			}
			
			// 퀵 정렬 시작!!!!!!
			quickSort(arr, 0, arr.length - 1);
		
			for (int x : arr) {
				sb.append(x).append(" ");
			}
			sb.append("\n");

		} // tc
		System.out.println(sb);
	}// main

	private static void quickSort(int[] arr, int left, int right) {
		if (left < right) {
			int pivot = partition(arr, left, right);
			quickSort(arr,left,pivot-1);
			quickSort(arr,pivot+1,right);
		}
	}

	private static int partition(int[] arr, int left, int right) {
		// 처음에 pivot을 오른쪽으로 
		int pivot = arr[right];
		int i = left - 1;
		
		// 배열을 보다가 pivot보다 작은게 나오면 i를 올리고 i위치랑 자리를 바꿈
		// i는 pivot보다 작은 값 개수, 
		for (int j = left; j < right; j++) {
			if (arr[j] <= pivot) {
				i++;
				swap(arr, i, j);
			}
		}
		//  pivot을 자기 위치로 보냄
		swap(arr, i + 1, right);
		return i + 1;
	}

	private static void swap(int[] arr, int a, int b) {
		int tmp = arr[a];
		arr[a] = arr[b];
		arr[b] = tmp;
	}
}
