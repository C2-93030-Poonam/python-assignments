// Write a java code to check if string is palindrome. 

import java.util.Scanner;

public class PalindromeChecker {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        
        System.out.print("Enter a string: ");
        String input = sc.nextLine();

        
        String cleaned = input.replaceAll("\\s+", "").toLowerCase();

        boolean isPalindrome = true;
        int len = cleaned.length();
        for (int i = 0; i < len / 2; i++) {
            if (cleaned.charAt(i) != cleaned.charAt(len - 1 - i)) {
                isPalindrome = false;
                break;
            }
        }

    
        if (isPalindrome) {
            System.out.println("The string is a palindrome.");
        } else {
            System.out.println("The string is not a palindrome.");
        }
    }
}