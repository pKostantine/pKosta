// Prompt the user for a number greater than 1 which will serve as your ending number. Your program will then count from
// the number 1 to the entered ending number. If the number is a multiple of 3, then the program prints Donut instead of
// the number. If the number is a multiple of 5, then it prints out Cookie instead of the number. If the number is a multiple
// of both 3 and 5 it prints out Bagel. Otherwise, it prints out the actual number
// • Sample Output: 1, 2, Donut, 4, Cookie, Donut, 7, 8, Donut, Cookie, 11, Donut, 13, 14, Bagel, 16, 17, Donut, 19, Cookie, Donut, etc.

import java.util.Scanner; 

public class QuestionC {
	public static void main(String[] args) {
	    Scanner userInput = new Scanner(System.in);
	    
	    int donutNumber = 3; 
	    int cookieNumber = 5; 
	    int endingNumber; 
	    int current = 1; 
	    
	    System.out.print("Enter ending number: ");
	    endingNumber = userInput.nextInt(); 
	    
	    while (current <= endingNumber) {
	        if (current % donutNumber == 0 && current % cookieNumber == 0) 
	            System.out.print("Bagel, ");
	        else if (current % donutNumber == 0)
	            System.out.print("Donut, ");
	        else if (current % cookieNumber == 0)
	            System.out.print("Cookie, ");
	        else 
	            System.out.print(current+", "); 
	       current ++;
	    }
	}
}