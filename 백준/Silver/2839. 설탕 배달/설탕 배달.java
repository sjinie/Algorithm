import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		int n = scanner.nextInt();
		
		if(n%5 == 0) {
			//5의 배수는 5a개가 가장 적음
			System.out.println(n/5);
			return;
		} else {
			//5a+3b꼴
			int a = n/5;
			//a가 최대가 되면서 3b 성립
			for(int i=a; i>0 ; i--) {
				int temp = n-(i*5);
				if(temp%3 == 0) {
					System.out.println(i+(temp/3));
					return;
				}
			}
		} 
		//3만 들고가는게 가장 적을때
		if(n%3==0) {
			System.out.println(n/3);
			return;
		} else {
			System.out.println(-1);
			return;
		}
	}
}