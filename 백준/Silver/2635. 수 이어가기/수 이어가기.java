import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		ArrayList<Integer> list = new ArrayList<>();
		ArrayList<Integer> listResult = new ArrayList<>();
		int N = Integer.parseInt(br.readLine()); // 4
		int result = 0;
		int max = 0;
		for (int i = N; i > 0; i--) {
			list.clear();

			list.add(N);
			list.add(i);
			int idx = 0;
			int num = 0;
			// 숫자 뺴기
			while (true) {
				num = list.get(idx) - list.get(idx + 1);
				if (num >= 0)
					list.add(num);
				else
					break;
				idx++;
			}

			if (max < list.size()) {
				max = list.size();
				listResult.clear();
				for(int x: list) {
					listResult.add(x);
				}
					
			}
		}
		System.out.println(max);
		for(int x : listResult) {
			System.out.print(x+" ");
		}
	
	}

}
