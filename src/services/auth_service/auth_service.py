import re
from src.display.print_colors.PrintColors import PrintColors

# This function enable to get the credentials for the account that will be used to send the emails
def login(config) :

    # Header
    print(PrintColors.BOLD + "=================================")
    print(" Login (Gmail account recommended)" + PrintColors.END)

    # Collect user input : email & app key
    email = input("Your email : ")
    password = input("Your application key : ")

    # Regex to validate the email
    EMAIL_REGEX = re.compile(
        r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    )

    # If the email is validated, add it to the config
    if email and EMAIL_REGEX.match(email):
        config["USER_EMAIL"] = email
    else : # Else print a validation error
        print(PrintColors.RED + "ValidationError : A valid email is mandatory ! " + PrintColors.END)

    # If the password is correctly set, add it to the config
    if password :
        config["USER_PASSWORD"] = password
    else : # Else print a validation error
        print(PrintColors.RED + "ValidationError : Application key is mandatory ! " + PrintColors.END)

    # If both verification passed : Login successful
    if config["USER_EMAIL"] and config["USER_PASSWORD"]:
        print(PrintColors.GREEN + " Login Success ! " + PrintColors.END)

    # Redirection to the main menu
    config["ROUTER"] = ""
    return config

# This function reset the account credentials
def logout(config):

    # Reset email & password values in the config
    config["USER_EMAIL"] = ""
    config["USER_PASSWORD"] = ""

    # Print a confirmation message
    print(PrintColors.GREEN + " Logout Success ! " + PrintColors.END)

    # Redirection to the main menu
    config["ROUTER"] = ""
    return config