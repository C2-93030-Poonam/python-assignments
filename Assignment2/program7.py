#Write a program that will calculate the price for a quantity entered from the keyboard, given that the
# unit price is Rs 5 and there is a discount of 10 percent for quantities over 30 and a 15 percent discount
# for qu antities over 50


UNIT_PRICE = 5

quantity = int(input("Enter the quantity: "))

base_price = quantity * UNIT_PRICE

if quantity > 50:
    discount_rate = 0.15
elif quantity > 30:
    discount_rate = 0.10
else:
    discount_rate = 0.0

discount_amount = base_price * discount_rate
final_price = base_price - discount_amount

print(f"\nQuantity: {quantity}")
print(f"Unit Price: Rs {UNIT_PRICE}")
print(f"Discount Applied: {discount_rate * 100:.0f}%")
print(f"Total Price after Discount: Rs {final_price:.2f}")