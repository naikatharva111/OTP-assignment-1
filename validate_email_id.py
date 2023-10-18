

def ValidateEmailID(Email):
    if "@gmail.com" not in Email:
        print("Please Enter Valid Email address!!")
        Email = input("Enter the Email:")
    return Email

    