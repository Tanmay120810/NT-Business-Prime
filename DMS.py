# User role selection
role = input("Select your role (dealer, staff, admin): ")
user_id = input("Enter your user ID: ")

# Password recovery operation
operation = input("If you forgot, select operation (id, password): ")
if operation == "id":
    print("Follow the steps to recover your ID.")
    outlet_number = input("Enter your outlet registered number: ")
    otp = input("Enter OTP: ")
    print("Your request answer is: Parashar Company")
    new_password = input("Enter your password: ")

# Purpose of contact
purpose = input("What is your purpose? (Press enter forpurpose): ")
operation = input("Enter operation (sales, service, development, stocks): ")

# Contact information based on operation
if operation == "sales":
    print("For sales-related works, contact our sales manager Mr. Rajesh \nContact: 9162309057")
elif operation == "service":
    print("For service-related works, contact our service center Ms. Divya & Company \nContact: 9162309057")
elif operation == "development":
    print("For development-related works, contact our development team at Parashar Development Team \nContact: 9162309057")
    print("Note: For development, your outlet should be 3 years old and more than 300 sq. ft. in area.")
elif operation == "stocks":
    print("For stocks-related works, visit Parashar Stocks of Spares \nor visit 'www.parasharstocks.com' \nContact: 9162309057")

# Stock check eligibility
stock_check = input("To check your stock, enter 'yes' or 'no': ")
if stock_check == "yes":
    print("you are not eligible for checking stocks\nto check stocks upgrade from AD POINT to AMD POINT")
k=input("thankyou to our dealers that you trust us")
    
