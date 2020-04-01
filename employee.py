import random
import string


employee_details = []
char = string.ascii_letters + string.digits

def get_employee_data():
    first_name = input("What is your first name?\n ")
    last_name = input("What is your last name?\n ")
    email = input("What is your email address?\n ")
    random_text = "".join(random.choice(char) for i in range(5))
    password = first_name[0:2]  + last_name[-2:] + random_text
    ans = ""
    while (ans != "n" and ans != "y"):
        ans = input(f"Do you prefer this '{password}' as password? (Y)es / (N)o ").lower()
    else:
        if ans == "n":
            password = None
            while (not password):
                password = password_check()
            else:
                ans == "y" # or pass
        store_employee_data(first_name, last_name, email, password)


def password_check():
    password = input("Please input your preferred password ")
    if len(password) < 7 :
        print("Password should be equal or greater than 7 ")
    else:
        print(f"This is the password '{password}' you chose")
        return password

def store_employee_data(*args):
    # Unpack arguments in the same order as inputted
    (first_name, last_name, email, password) = args
    details = {}
    details["First name"] = first_name
    details["Last name"] = last_name
    details["Email"] = email
    details["Password"] = password
    # this could also be done with details= {"First name": first_name, "Last name": last_name ....}
    employee_details.append(details)
    display_all_employees()
    
def display_all_employees():
    should_continue = input("Continue? (Y)es or Any other letter to quit ").lower()
    if should_continue == "y":
        get_employee_data()       
    else:
        for employee in employee_details:
            print(f"DETAILS FOR USER {employee['First name']}")
            for det, val in employee.items():
                print(f"\t {det}: {val}")
            print("")
                
get_employee_data()
