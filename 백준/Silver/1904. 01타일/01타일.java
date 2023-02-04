import java.io.*;

public class Main {

  private static int[] tile; 

  public static void main(String[] args) throws IOException{
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    int n = Integer.parseInt(br.readLine());

    tile = new int[10000001];

    bw.write(String.valueOf(tiling(n)));

    bw.flush();
    bw.close();
  }

  private static int tiling(int n) {
    if(tile[n] > 0) return tile[n]; // 이전에 계산했던 값이라면 중복 계산을 하지 않는다.

    if (n == 1) return tile[1] = 1;
    else if (n == 2) return tile[2] = 2;
    else if (n == 3) return tile[3] = 3;
    else {
        tile[n] = tiling(n-1) + tiling(n-2);
        return tile[n] %= 15746;
    }
  }
}