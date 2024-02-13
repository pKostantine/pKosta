// Write a program that will sum up all the numbers from question #7 and print out the
// total.


import java.util.Scanner; 
public class Eight {
	public static void main(String [] args) {
		Scanner userInput = new Scanner(System.in);
		
		int startNumber; 
		int endNumber ;
		int total=0;
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
//			System.out.print(currentCube + " ");
			total += currentCube;  // total = total + currentCube 
		}
		
		int finalTotal=startNumber+endNumber+total;
		System.out.println(finalTotal);
	}
}