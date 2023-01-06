import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int N, M, day;
    static int[] dr = {-1, 0, 1, 0}, dc = {0, 1, 0, -1};
    static int[][] map;
    static boolean[][] visited;
    static ArrayList<int[]> site;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        M = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());

        map = new int[N][M];
        visited = new boolean[N][M];
        day = 0;
        site = new ArrayList<>();

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
                if (map[i][j] == 1) {
                    site.add(new int[]{i, j});
                }
            }
        }
        DFS();
        for(int i=0;i<N;i++){
            for(int j=0;j<M;j++){
                if(!visited[i][j]&&map[i][j]==0) {
                    System.out.println("-1");
                    return;
                }
            }
        }
        if(day!=0) System.out.println(day-1);
        else System.out.println(day);
    }

    private static void DFS() {
        Queue<int[]> que = new LinkedList<>();
        for (int i = 0; i < site.size(); i++) {
            que.add(site.get(i));
            visited[site.get(i)[0]][site.get(i)[1]] = true;
        }
        while (!que.isEmpty()) {
            int[] curr = que.poll();
            for (int k = 0; k < 4; k++) {
                int nr = curr[0] + dr[k];
                int nc = curr[1] + dc[k];
                if (nr >= 0 && nc >= 0 && nr < N && nc < M) {
                    if (map[nr][nc] == 0 && !visited[nr][nc]) {
                        visited[nr][nc] = true;
                        map[nr][nc] = map[curr[0]][curr[1]] + 1;
                        if (day < map[nr][nc])
                            day = map[nr][nc];
                        que.add(new int[]{nr, nc});
                    }
                }
            }
        }
    }
}
