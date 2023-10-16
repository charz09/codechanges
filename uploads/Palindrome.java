public class Palindrome {
    public static void main(String[] args) {
        if (args.length != 1) {
            System.err.println("Please provide exactly one command line argument.");
            System.exit(1);
        }
        
        String input = args[0];
        String sanitizedInput = sanitizeInput(input);
        
        if (isPalindrome(sanitizedInput)) {
            System.out.println("The input is a palindrome.");
        } else {
            System.out.println("The input is not a palindrome.");
        }
    }
    
    private static String sanitizeInput(String input) {
        // Remove all non-alphanumeric characters and convert to lowercase
        return input.replaceAll("[^a-zA-Z0-9]", "").toLowerCase();
    }
    
    private static boolean isPalindrome(String input) {
        int left = 0;
        int right = input.length() - 1;
        
        while (left < right) {
            if (input.charAt(left) != input.charAt(right)) {
                return false;
            }
            left++;
            right--;
        }
        
        return true;
    }
}
