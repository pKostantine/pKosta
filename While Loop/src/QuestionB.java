// Have the user enter a number greater than 1. Your program should then print out the factors of that number.
// • Sample Output: if the user enters 24, then your program should output: 1,2,3,4,6, 8, 12, 24.

import java.util.Scanner; 
public class QuestionB {
	public static void main(String [] args) {
		Scanner userInput = new Scanner(System.in);
		
		int targetNumber; 
		int current = 1; 
		
		System.out.print("Enter number: ");
		targetNumber = userInput.nextInt(); 
		
		while (current <= targetNumber) {
			if (targetNumber % current == 0) {
				System.out.print(current+" ");
			}
			current++;
		}
		System.out.println("Have a nice day!");
	}
}