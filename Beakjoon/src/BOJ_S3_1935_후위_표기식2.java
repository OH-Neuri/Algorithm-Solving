import java.io.*;
import java.util.Stack;

public class BOJ_S3_1935_후위_표기식2 {

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		// 피연산자 개수
		int num = Integer.parseInt(br.readLine());
		// 후위표기식
		String str = br.readLine();
		// 문자에 해당하는 숫자
		double[] arr = new double[num];
		for (int i = 0; i < arr.length; i++) {
			arr[i] = Double.parseDouble(br.readLine());
		}

		double result = 0;
		Stack<Double> stack = new Stack<>();
		// 피연산자일경우 push, 연산자일경우 연산 후 push
		for (int i = 0; i < str.length(); i++) {
			if ('A' <= str.charAt(i) && str.charAt(i) <= 'Z') {
				stack.push(arr[str.charAt(i) - 'A']);
			} else {
				double first = stack.pop();
				double second = stack.pop();
				switch (str.charAt(i)) {
				case '+':
					result = second + first;
					stack.push(result);
					continue;
				case '-':
					result = second - first;
					stack.push(result);
					continue;
				case '*':
					result = second * first;
					stack.push(result);
					continue;
				case '/':
					result = second / first;
					stack.push(result);
					continue;
				}

			}
		}
		System.out.printf("%.2f", stack.pop());
		br.close();
	}
}
