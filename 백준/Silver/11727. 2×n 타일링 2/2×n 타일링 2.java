import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] D = new int[1001];

        D[1] = 1;
        D[2] = 3;

        for (int i = 3; i <= n; i++) {
            D[i] = (D[i - 1] + 2 * D[i - 2])%10007;
        }
        System.out.println(D[n]);

    }
}
