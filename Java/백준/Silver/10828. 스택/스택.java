import java.util.Scanner;


public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		
		int flag = sc.nextInt();
		sc.nextLine(); // 엔터 키 입력을 소비하기 위한 코드

		String[] command = new String[flag+1];
				
		for(int i=0;i <flag;i ++) {
			
			command[i]= sc.nextLine();
			
		}

		int[] stack = new int[flag];
		int top = -1;
		
		int sizestack = 0;
		int num = 0;
		int bufflag = 0;
		
		for(int i=0;i < flag;i ++) {
			
			switch (command[i]) {
			
			case "pop":
				if(top == -1) {
					System.out.println(-1);
				}else {
					System.out.println(stack[top]);
					stack[top]=0;
					top--;
				}
				break;
				
			case "size":
				System.out.println(top+1);
				break;
				
			case "empty":
				if(top == -1) {
					System.out.println(1);

				}else {
					System.out.println(0);

				}
				break;
				
			case "top":
				if(top == -1) {
					System.out.println(-1);

				}else {
					System.out.println(stack[top]);
				}
				break;
				
			default:
				String[] pushnum = command[i].split(" ");
				
				num = Integer.parseInt(pushnum[1]);
				
				top++;
				
				stack[top]=num;
				
				break;
			}	
		}
		

	}

}