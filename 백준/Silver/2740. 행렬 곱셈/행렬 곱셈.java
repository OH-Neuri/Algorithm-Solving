import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] string = br.readLine().split(" ");
		int n = Integer.parseInt(string[0]);
		int m = Integer.parseInt(string[1]);
		int[][] a = new int[n][m];
		for (int i=0; i<n; i++) {
			string = br.readLine().split(" ");
			for (int l = 0; l<m; l++) {
				a[i][l] = Integer.parseInt(string[l]);
			}
		}
		
		string = br.readLine().split(" ");
		int k = Integer.parseInt(string[1]);
		int[][] b = new int[m][k];
		for (int i=0; i<m; i++) {
			string = br.readLine().split(" ");
			for (int l=0; l<k; l++) {
				b[i][l] = Integer.parseInt(string[l]);
			}
		}
		
		int sum;
		for (int i=0; i<n; i++) {
			if (i!=0) System.out.println();
			for (int l=0; l<k; l++) {
				sum = 0;
				for (int p=0; p<m; p++) {
					sum += a[i][p]*b[p][l];
				}
				System.out.print(sum + " ");
			}
		}
	}
}
