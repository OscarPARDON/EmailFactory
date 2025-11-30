from src.display.email_conf_menu.email_conf_menu import display_email_config_menu

# Email configuration router
def email_config(config):

    # Call the menu display function and get the user choice
    choice = display_email_config_menu(config)

    # Link Numbers to the routes
    match choice :
        case "1":
            config["ROUTER"] = "set_email_subject"
        case "2":
            config["ROUTER"] = "set_email_body"
        case "3":
            config["ROUTER"] = "add_attachment"
        case "4":
            config["ROUTER"] = "reset_attachments"
        case _ :
            config["ROUTER"] = ""

    return config
