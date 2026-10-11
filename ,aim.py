
while True:
    try:
        bill = float(input("Enter the total shopping bill: ₹"))
        if bill <= 0:
            print("Bill must be greater than zero.")
            continue
        break
    except ValueError:
        print("Invalid input! Please enter a number.")

while True:
    try:
        discount = float(input("Enter discount percentage: "))
        if discount < 0 or discount > 100:
            print("Discount must be between 0 and 100.")
            continue
        break
    except ValueError:
        print("Invalid input! Please enter a number.")

while True:
    try:
        people = int(input("Enter number of people: "))
        if people <= 0:
            print("Number of people must be positive.")
            continue
        break
    except ValueError:
        print("Invalid input! Enter a whole number.")

discount_amount = bill * discount / 100
final_bill = bill - discount_amount
amount_per_person = final_bill / people

print("\n----- BILL SUMMARY -----")
print(f"Original bill: ₹{bill:.2f}")
print(f"Discount: {discount}%")
print(f"Discount amount: ₹{discount_amount:.2f}")
print(f"Final bill: ₹{final_bill:.2f}")
print(f"Each person pays: ₹{amount_per_person:.2f}")
