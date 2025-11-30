from src.display.print_colors.PrintColors import PrintColors

# Display the server configuration menu
def display_server_config_menu():

    # Header
    print(PrintColors.BOLD + "===================================")
    print("Server Configuration " + PrintColors.END)

    # Choices
    print("Please choose an option :")
    print(PrintColors.BLUE + " 0 : Go Back " + PrintColors.END)
    print(PrintColors.YELLOW + " 1 : Change Server Address")
    print(" 2 : Change Port")
    print(" 3 : Change Randomizer Settings" + PrintColors.END)

    return input("Enter your choice (0-3) : ")