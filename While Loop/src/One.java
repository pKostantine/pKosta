//Prompt the user how many “Hello World” greetings they wish, and then use a while
//loop to display ”Hello World” the entered number of times.

import java.util.Scanner; 

public class One {
	public static void main (String [] args) {
		Scanner userInput = new Scanner(System.in);
		
		int nGreetings;
		int count=0;
		
		System.out.println("How many times should I say hi? ");
		nGreetings=userInput.nextInt();
		
		while (count<nGreetings) {
			System.out.println("Hello World!");
			count++;
		}
		
//		for (int i=0;i<nGreetings;i++) {
//			System.out.println("Hello World!");
//		}
		
		System.out.println("Have a nice day!");
		
	}
}
