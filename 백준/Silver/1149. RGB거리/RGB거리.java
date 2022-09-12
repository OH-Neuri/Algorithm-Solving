import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws NumberFormatException, IOException {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int n = Integer.parseInt(br.readLine());
		int[][] nums = new int[n][3];
		
		for (int i=0; i<n; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			for (int j=0; j<3; j++) {
				nums[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		for (int i=1; i<n; i++) {
			nums[i][0] += Math.min(nums[i-1][1], nums[i-1][2]);
			nums[i][1] += Math.min(nums[i-1][2], nums[i-1][0]);
			nums[i][2] += Math.min(nums[i-1][0], nums[i-1][1]);
		}
		
		
		System.out.println(Math.min(nums[n-1][0], Math.min(nums[n-1][1], nums[n-1][2])));
	}
}