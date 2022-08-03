import java.util.Scanner;

public class 달팽이는_올라가고싶다{
	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);

		int a = sc.nextInt();
		int b = sc.nextInt();
		int c = sc.nextInt();

		int day = (c - b) / (a - b);
		if ((c - b) % (a - b) != 0) {
			System.out.println(day + 1);
		} else {
			System.out.println(day);

		}

	}
}