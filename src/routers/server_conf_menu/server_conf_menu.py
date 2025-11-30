from src.display.server_conf_menu.server_conf_menu import display_server_config_menu

# Server configuration router
def server_config(config):

    # Call the menu display function and get the user choice
    choice = display_server_config_menu(config)

    # Link the numbers to the routes
    match choice :
        case "1":
            config["ROUTER"] = "set_server_address"
        case "2":
            config["ROUTER"] = "set_port"
        case "3":
            config["ROUTER"] = "set_randomizer"
        case _:
            config["ROUTER"] = ""

    return config
