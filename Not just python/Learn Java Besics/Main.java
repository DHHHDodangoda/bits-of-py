// Import scanner

import java.util.Scanner; // Over

// Start

public class Main {

	public static void main(String[] args) {
		
		// Display text with print or println
		
		System.out.println("\"Hello!\"\n");
		System.out.println("\tTest");
		
		// Data types and store values to them
		
		int X = 12234;
		long x =546548465215845L;
		float Y = 3.457F;
		double y = 3.45745782;
		
		// Display them for test
		
		System.out.println(X);
		System.out.println(x);
		System.out.println(Y);
		System.out.println(y);
		System.out.println("My number is: "+x);
		
		// More variables
		
		boolean Z = true;
		boolean z = false;
		char Symbol = '@';
		String name= "Hiruna";
		
		// Display them
		
		System.out.println(Z);
		System.out.println(z);
		System.out.println(Symbol+" Home");
		System.out.println("Hello "+name);
		System.out.println(Symbol+name);
		
		// Switching values of variables
		
		String A = ("Water");
		String B = ("Soda");
		String temp;
		
		// process 
		
		temp = A;
		A = B;
		B = temp;
		
		// Display the result
		
		System.out.println("A: "+A);
		System.out.println("B: "+B);  // Fixed semicolon to colon
		
		// Using scanner 
		
		try (Scanner scanner = new Scanner(System.in)) {
		
			// Use scanner to take inputs from user
			
			System.out.println("What is your name? ");
			String Name = scanner.nextLine();
			
			System.out.println("How old are you? ");
			int age = scanner.nextInt();
			
			//To fix the below error add empty nextLine to read and remove the \n
			
			scanner.nextLine(); // Error fix
			
			System.out.println("What is your favorite food? ");
			String food = scanner.nextLine();
			
			/* But there is an error here.
			 * After the nextInt there is a \n left in the scanner. 
			 * Since nextInt can't read it, you have to remove the \n to fix this error.
			 */
			
			
			// Display the input
			
			System.out.println("Hello "+Name);
			System.out.println("You are "+age+" years old");
			System.out.println("You like "+food);
		}
		
		/* Learn about expression
		 * Expression = operands + operators
		 * 
		 * operands = values,variables,numbers,quantity
		 * operators = + - * / %
		 */
		
		int friends = 10;
		
		friends = friends + 5;
		
		System.out.println(friends);
		
		double Friends = 110;
		
		Friends = Friends / 3;
 		
		System.out.println(Friends);
		
		// +1 to value
		
		friends++;
		
		System.out.println(friends);
		
		// -1 to value
		
		friends--;
		
		System.out.println(friends);
		
		// scanner.close(); // Removed as try-with-resources automatically closes it
	}

}
