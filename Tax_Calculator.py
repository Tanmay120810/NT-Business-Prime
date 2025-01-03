def calculate_tax(income):
    tax = 0

    # Define tax slabs and rates
    if income <= 250000:
        tax = 0
    elif income <= 500000:
        tax = (income - 250000) * 0.05
    elif income <= 1000000:
        tax = (500000 - 250000) * 0.05 + (income - 500000) * 0.20
    else:
        tax = (500000 - 250000) * 0.05 + (1000000 - 500000) * 0.20 + (income - 1000000) * 0.30

    return tax


def main():
    while True:
        try:
            # Input income from the user
            income = float(input("Enter your annual income (₹): "))
            
            # Check for negative income
            if income < 0:
                print("Income can't be negative. Please enter a valid income.")
                continue

            # Calculate tax
            tax = calculate_tax(income)

            # Display the tax
            print(f"Your total income tax is: ₹{tax:.2f}")

        except ValueError:
            print("Invalid input. Please enter a valid number.")

        # Ask the user if they want to continue
        again = input("Do you want to calculate tax for another income? (yes/no): ").lower()
        if again != 'yes':
            print("Thank you for using the tax calculator!")
            break


if __name__ == "__main__":
    main()
