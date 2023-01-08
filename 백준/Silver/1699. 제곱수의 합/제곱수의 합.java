import java.util.*;
import java.math.*;
public class Main {
	
	static long dp[] ;
	
	public static void main(String[] args)   {
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		dp = new long[100001];
		dp[1] =1;
		for(long i=2;i<=n;i++) {	
			for(long j=1;j<i;j++) {
				long x = i-j; 
				long com =x*x;
				if(com==i) dp[(int) i] = 1; 
				else if(com< i) { 
					if(dp[(int) i]==0) { 
						
						dp[(int) i] = dp[(int) (x*x)] + dp[(int) (i-(com))];
					}
					else dp[(int) i] = Math.min(dp[(int) com] + dp[(int) (i-(com))],dp[(int) i]);
				}
				else continue;
			}

		}
		
		System.out.println(dp[n]);
			
	}
	
}