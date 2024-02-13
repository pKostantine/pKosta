// Print out the first 10 cubes: (1, 8, 27, 64 etc)

public class Four {
	public static void main (String [] args) {

		int count=1;
		
		while (count<=10) {
			System.out.println(Math.pow(count,3));
			count++;
		}
	}
}
