// Write a program that will prompt the user for a number greater than 1. Your program will then count off all the numbers
// from 1 to their number and output each number as even or odd.
// • Sample Output: 1 is odd, 2 is even, 3 is odd, 4 is even, 5 is odd, and so on until the user entered number is entered.

import java.util.Scanner; 
public class QuestionA {
	public static void main(String [] args) {
		Scanner userInput = new Scanner(System.in);
		
		int startNumber; 
		int endNumber ;
		int total = 0; 
		double currentCube; 

		System.out.print("Enter start number: ");
		startNumber = userInput.nextInt(); 
		do {
			System.out.print("Enter ending number: ");
			endNumber = userInput.nextInt(); 
			
			if (endNumber <= startNumber) {
				System.out.println("End number needs to be at least "+(startNumber+1));
			}
			
		} while (endNumber <= startNumber);
		
		for (int i = startNumber; i <= endNumber; i++) {
			currentCube = Math.pow(i, 3);
			System.out.print(currentCube + " ");
			total += currentCube;  // total = total + currentCube 
		}
		
		System.out.println("\nThank you for counting from "+startNumber+" to "+endNumber+"\nThe total of the numbers is: "+total+"\nHave a nice day!");
	}
}