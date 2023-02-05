import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] cardPack = new int[n+1];
        int[] maxArr = new int[n+1];
        cardPack[0] = 0;
        StringTokenizer st = new StringTokenizer(br.readLine());

        for(int i = 1 ; i <= n ; i++) {
            cardPack[i] = Integer.parseInt(st.nextToken());
        }

        for(int i = 1; i <=n; i++) {
            for(int j = 1; j <=i; j++) {
                maxArr[i] = Math.max(maxArr[i],cardPack[j]+maxArr[i-j]);
            }
        }
        System.out.println(maxArr[n]);
    }

}