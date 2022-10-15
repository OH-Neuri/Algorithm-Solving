import java.util.*;


class Main
{
	static int[] mem;	//숫자 맴버
	static int[] visit;
	static int k;
	public static void main (String[] args)
	{
		Scanner sc = new Scanner(System.in);
		while(true)
		{
			k = sc.nextInt();
			
			if(k == 0) break;
			visit = new int[k];
			mem = new int[k];
			
			for(int i = 0 ; i < k ; i++)
			{
				mem[i] = sc.nextInt();	//맴버를 받아오고 경우의 수를 만들어야함
			}
			
			recursive(0,0);
			System.out.println();
		}
	}
	static void recursive(int start ,  int len)
	{
		
		if(len == 6)
		{
			for(int i = 0 ; i < k ; i++)
			{
				if(visit[i] == 1)
				{
					System.out.print(mem[i]+ " ");
				}
			}
			System.out.println();
		}
		else
		{
			for(int i = start ; i < k ; i++)
			{
				if(visit[i] == 0)
				{
					//한 번도 안 썼다
					visit[i] = 1;
					recursive(i,len+1);
					visit[i] = 0;
				}
			}
		}
		
	}
}
