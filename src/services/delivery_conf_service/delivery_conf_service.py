import re
import shutil
from src.display.print_colors.PrintColors import PrintColors

# This function enables to load an email list to which send the email
def set_delivery_list(config):

    # Header
    print(PrintColors.BOLD + "=================================")
    print(" Load an email list (txt only) " + PrintColors.END)

    # If a list is already loaded : ask for permission to replace it
    if config["GET_DELIVERY_LIST"]:
        check = input("Are you sure that you want to change the currently loaded list ? [y / n] : ")
    else :
        check = "y"

    # If the user want to add or replace the list ...
    if check == "y" :

        # Ask for the absolute path to the list on the user computer
        path = input("Please enter the absolute path of the txt file : ")

        # Regex to verify that the path is an absolute path to a txt file
        PATH_REGEX = re.compile(r"^/.*\.txt$")

        # If the path is validated, try to load it to the designated storage spot
        if path and PATH_REGEX.match(path):

            try :
                # Try to copy the list to the designated storage spot
                shutil.copy(path, "email_list/email_list.txt")
                # Inform the config that a list has been loaded
                config["GET_DELIVERY_LIST"] = 1
                # Print confirmation
                print(PrintColors.GREEN + "Delivery list successfully loaded ! " + PrintColors.END)

            # Error handling
            except Exception as e:
                print(PrintColors.RED + e + PrintColors.END)

        else : # If the path is not valid : raise a validation error
            print(PrintColors.RED + "ValidationError : A valid absolute path to a txt file is mandatory ! " + PrintColors.END)

    # Redirection to the main menu
    config["ROUTER"] = ""
    return config