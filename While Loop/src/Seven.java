// Prompt the user for a starting and ending number. Ensure that the ending number is
// greater than the starting number. Output all the numbers from the starting value to
// the ending value.

import java.util.Scanner; 
public class Seven {
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