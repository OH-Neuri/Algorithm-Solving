import java.io.*;
import java.util.*;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] dp = new int[11];
        dp[2] = 1;
        for (int i = 3; i <= n; i++) {
            dp[i] = i-1 + dp[i-1];
        }
        System.out.print(dp[n]);
    }
}