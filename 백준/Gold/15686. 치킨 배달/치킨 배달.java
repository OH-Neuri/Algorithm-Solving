import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;
 
public class Main {
    static int N, M, min = Integer.MAX_VALUE;
    static ArrayList<int[]> chickenStore;
    static int isSelected[], city[][];
 
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
 
        city = new int[N][N];
        chickenStore = new ArrayList<int[]>();
        for (int r = 0; r < N; r++) {
            st = new StringTokenizer(br.readLine());
            for (int c = 0; c < N; c++) {
                city[r][c] = Integer.parseInt(st.nextToken());
                if (city[r][c] == 2)
                    chickenStore.add(new int[]{r, c});
            }
        }
 
        isSelected = new int[M];
        comb(0, 0);
 
        System.out.println(min);
    }
 
    // 치킨 집 고르기
    private static void comb(int cur, int cnt) {
        if (cnt == M) {
            min = Math.min(min, checkLength());
            return;
        }
 
        for (int i = cur; i < chickenStore.size(); i++) {
            isSelected[cnt] = i;
            comb(i + 1, cnt + 1);
        }
    }
 
    // 치킨 거리 구하기
    private static int checkLength() {
        int sum = 0;
 
        for (int r = 0; r < N; r++) {
            for (int c = 0; c < N; c++) {
                if (city[r][c] == 1) {
                    int min_length = Integer.MAX_VALUE;
                    for (int k = 0; k < M; k++) {
                        int[] chicken = chickenStore.get(isSelected[k]);
                        int d = Math.abs(r - chicken[0]) + Math.abs(c - chicken[1]);
                        min_length = Math.min(min_length, d);
                    }
                    sum += min_length;
                }
            }
        }
 
        return sum;
    }
}