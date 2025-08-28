#Write a program that prompts the user to 
# input number of calls and calculate the monthly
#  telephone
# bills as per the following rule:
#Minimum Rs. 200 for up to 100 calls.
# Plus Rs. 0.50 per call for next 50 calls.
# Plus Rs. 0.40 per call for any call beyond 200 calls


calls = int(input("Enter the number of calls made this month: "))

bill = 200  

if calls > 100:
    extra_calls = calls - 100

    if extra_calls <= 50:
        bill += extra_calls * 0.60
    else:
        bill += 50 * 0.60
        extra_calls -= 50

        if extra_calls <= 50:
            bill += extra_calls * 0.50
        else:
            bill += 50 * 0.50
            extra_calls -= 50
            bill += extra_calls * 0.40


print(f"Your total telephone bill is: Rs. {bill:.2f}")