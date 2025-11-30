from src.display.print_colors.PrintColors import PrintColors

# Display the email configuration menu
def display_email_config_menu(config):

    # Header
    print(PrintColors.BOLD + "====================================")
    print("Email Configuration" + PrintColors.END)

    # Choices
    print("Please choose an option : ")
    print(PrintColors.BLUE + " 0 : Go Back " + PrintColors.END)

    if config["SUBJECT"]:
        print(PrintColors.YELLOW + " 1 : Change Email Subject " + PrintColors.END)
    else:
        print(PrintColors.RED + " 1 : Setup Email Subject " + PrintColors.END)

    if config["GET_BODY"]:
        print(PrintColors.YELLOW + " 2 : Change Email Body " + PrintColors.END)
    else:
        print(PrintColors.RED + " 2 : Load Email Body " + PrintColors.END)

    print(PrintColors.PURPLE + " 3 : Add Attachment " + PrintColors.END)

    if len(config["ATTACHMENTS"]) > 0:
        print(PrintColors.RED + " 4 : Reset Attachments " + PrintColors.END)

    if not (config["GET_BODY"] and config["SUBJECT"]):
        print(PrintColors.RED + " Need configuration ! " + PrintColors.END)

    if len(config["ATTACHMENTS"]) > 0:
        return input("Enter your choice (0-4) : ")
    else :
        return input("Enter your choice (0-3) : ")