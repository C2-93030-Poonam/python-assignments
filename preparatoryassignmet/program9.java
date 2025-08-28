# Write a java program to accept a number from user using command line 
#argument and display its table. 

import java.util.Scanner;

public class Test {

    
    static String toOctal(int num) {
        if (num == 0) return "";
        return toOctal(num / 8) + (num % 8);
    }

    static String toHex(int num) {
        if (num == 0) return "";
        int rem = num % 16;
        char hexChar = (rem < 10) ? (char) ('0' + rem) : (char) ('A' + rem - 10);
        return toHex(num / 16) + hexChar;
    }

    
    static String toBinary(int num) {
        StringBuilder binary = new StringBuilder();
        for (int i = 31; i >= 0; i--) {
            int bit = (num >> i) & 1;
            if (binary.length() > 0 || bit == 1) {
                binary.append(bit);
            }
        }
        return binary.length() == 0 ? "0" : binary.toString();
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter Number : ");
        int number = sc.nextInt();

        System.out.println("Given Number : " + number);
        System.out.println("Binary equivalent      : " + toBinary(number));
        System.out.println("Octal equivalent       : " + (number == 0 ? "0" : toOctal(number)));
        System.out.println("Hexadecimal equivalent : " + (number == 0 ? "0" : toHex(number)));
    }
}