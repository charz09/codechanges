// package import missing
import java.util.Scanner;

public class RewriteNumber {
	public static void main( String args[] ) {
	    Scanner in = new Scanner( System.in );

	    System.out.println( "Enter an integer between 0 and 9" );
	    int num = in.nextInt();

	    System.out.println( "You entered " + num );


		/*
		Using if and if-else statements
		*/
		String outString = "";
	    if ( num == 0 ) {
	    	outString = "zero" ;
	    } else if ( num == 1 ) {
	    	outString = "one" ;
	    } else if ( num == 2 ) {
	    	outString = "two" ;
	    } else if ( num == 3 ) {
	    	outString = "three" ;
	    } else if ( num == 4 ) {
	    	outString = "four" ;
	    } else if ( num == 5 ) {
	    	outString = "five" ;
	    } else if ( num == 6 ) {
	    	outString = "six" ;
	    } else if ( num == 7 ) {
	    	outString = "seven" ;
	    } else if ( num == 8 ) {
	    	outString = "eight" ;
	    } else if ( num == 9 ) {
	    	outString = "nine" ;
	    } else {
	    	outString = "invalid input" ;
	    }
		System.out.println( "You entered " + outString );


		/*
		Using a SWITCH statement
		*/
	    String numString = "";
        switch (num) {
            case 0:  numString = "zero";
                     break;
            case 1:  numString = "one";
                     break;
            case 2:  numString = "two";
                     break;
            case 3:  numString = "three";
                     break;
            case 4:  numString = "four";
                     break;
            case 5:  numString = "five";
                     break;
            case 6:  numString = "six";
                     break;
            case 7:  numString = "seven";
                     break;
            case 8:  numString = "eight";
                     break;
            case 9:  numString = "nine";
                     break;
            default: numString = "invalid input";
                     break;
        }
        System.out.println( "You entered " + numString );

		/*
		Using an array of Strings
		*/
		String [] myNums = { "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine" };

		if( num >= 0 && num <= 9 ) {
			System.out.println( "You entered " + myNums[num] );
		} else {
			System.out.println( "invalid input" );
		}



	}
}
