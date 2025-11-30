from src.display.main_menu.main_menu import display_main_menu
from src.services.file_service.file_service import clean_all_dirs
from src.services.sender_service.mailing_service import check_config

# Main menu router
def main_menu(config):

    # Call the menu display function and get the user choice
    choice = display_main_menu(config)

    # Link Numbers to the routes
    match choice :
        case "0":
            clean_all_dirs()
            config["DISPLAY"] = 0
        case "1":
            if config["USER_EMAIL"] and config["USER_PASSWORD"] :
                config["ROUTER"] = "logout"
            else :
                config["ROUTER"] = "login"
        case "2":
            config["ROUTER"] = "set_delivery_list"
        case "3":
            config["ROUTER"] = "email_config"
        case "4" :
            config["ROUTER"] = "server_config"
        case "5" :
            config = check_config(config)
        case _ :
            config["ROUTER"] = ""

    return config