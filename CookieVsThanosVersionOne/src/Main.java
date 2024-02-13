// Cookie vs Thanos - Pierre Kostantine - 09/02/2023

import java.util.Scanner;
import java.util.Random;

public class Main {
	public static int randIntBetween(int low,int high) {
		Random rand=new Random();
		if (low>=high)
			throw new IllegalArgumentException("High value must be greater than low value!");
		return rand.nextInt(high-low+1)+low;
	}
	
	public static int rollNDiceXSides(int numberOfSides,int numberOfTimes) {
		int total=0;
		for (int i=0; i < numberOfTimes; i++) {
			total += randIntBetween(1,numberOfSides);
		}
		return total;
	}
	
	public static void main(String [] args) {
		Scanner userInput=new Scanner(System.in);
		int thanosPoints=100;
		int cookiePoints=100;
		int thanosRoll;
		int cookieRoll;
		int roundNumber=1;
		int totalRounds;
		
		System.out.println("Welcome to the game...How many rounds will they battle? ");
		totalRounds=userInput.nextInt();
		
		while (roundNumber<=totalRounds) {
			thanosRoll=rollNDiceXSides(2,8);
			cookieRoll=rollNDiceXSides(3,6);
			System.out.println("Cookie Roll:\t"+cookieRoll+"\tThanos Roll:\t"+thanosRoll+"\nCookie Points:\t"+cookiePoints+"\tThanos Points:\t"+thanosPoints);
			
			if (thanosRoll>cookieRoll) {
				System.out.println("Thanos wins the round!\n");
				cookiePoints-=thanosRoll;
			}
			else if (thanosRoll<cookieRoll) {
				System.out.println("Cookie wins the round!\n");
				thanosPoints-=cookieRoll;
			}
			else
				System.out.println("The round is a tie! Points remain.\n");
			
			if (cookiePoints<=0||thanosPoints<=0)
				break;
			
			roundNumber++;
		}
		
		if (thanosPoints>cookiePoints)
			System.out.println("Thanos captures the Cookie Stone!");
		else if (thanosPoints<cookiePoints)
			System.out.println("Cookie Monster defends the Cookie Stone!");
		else
			System.out.println("The game ends in a tie!");
	}
}
