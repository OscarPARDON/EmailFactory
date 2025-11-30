from src.display.print_colors.PrintColors import PrintColors

# Display the main menu
def display_main_menu(config) :

    # Header
    print(PrintColors.BOLD + "====================================")
    print("Welcome on the Email Factory " + PrintColors.END)

    # Choices
    print("Please choose an option : ")
    print(PrintColors.BLUE + " 0 : Exit " + PrintColors.END)

    if config["USER_EMAIL"] and config["USER_PASSWORD"]:
        print(PrintColors.YELLOW + " 1 : Logout " + PrintColors.END)
    else :
        print(PrintColors.RED + " 1 : Log In " + PrintColors.END)

    if config["GET_DELIVERY_LIST"]:
        print(PrintColors.GREEN + " 2 : Delivery List Configuration " + PrintColors.END)
    else :
        print(PrintColors.RED + " 2 : Delivery List Configuration " + PrintColors.END)

    if config["GET_BODY"] and config["SUBJECT"] :
        print(PrintColors.GREEN + " 3 : Email Configuration " + PrintColors.END)
    else :
        print(PrintColors.RED + " 3 : Email Configuration " + PrintColors.END)

    print(PrintColors.YELLOW + " 4 : Server Configuration " + PrintColors.END)

    if config["USER_EMAIL"] and config["USER_PASSWORD"] and config["GET_DELIVERY_LIST"] and config["GET_BODY"] and config["SUBJECT"]:
        print(PrintColors.PURPLE + " 5 : Start Sending " + PrintColors.END)
        return input("Enter your choice (0-5) : ")
    else :
        print(PrintColors.RED + " Need configuration ! " + PrintColors.END)
        return input("Enter your choice (0-4) : ")