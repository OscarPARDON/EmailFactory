from src.routers.main_menu.main_menu import main_menu
from src.services.auth_service.auth_service import login, logout
from src.services.delivery_conf_service.delivery_conf_service import set_delivery_list
from src.services.email_conf_service.email_conf_service import set_subject, set_body, reset_attachments, new_attachment
from src.services.file_service.file_service import clean_dir
from src.services.sender_service.mailing_service import auto_mailer
from src.routers.email_conf_menu.email_conf_menu import email_config
from src.routers.server_conf_menu.server_conf_menu import server_config
from src.services.server_conf_service.server_conf_service import set_server_address, set_server_port, set_randomizer

# Initialisation of the configuration
def init_config():

    config = {
        "DISPLAY": 1,
        "ROUTER": "",
        "USER_EMAIL": "",  # Email of the user account, Mandatory
        "USER_PASSWORD": "",  # The application key to access the account, Mandatory
        "SERVER": "smtp.gmail.com",  # SMTP Server Address : By default is Gmail SMTP server
        "PORT": 465,  # Port used to send the emails, by default SMTP 465
        "GET_DELIVERY_LIST": 0,  # Boolean : Did a delivering list has been loaded ? Mandatory
        "GET_BODY": 0,  # Boolean : Did a body for the email has been loaded ? Mandatory
        "SUBJECT": "",  # Email subject : Empty by default, Mandatory
        "ATTACHMENTS": [],  # Attachments List : Empty by default
        "RANDOMIZER_MIN": 2,  # Default value : wait minimum 2s between each email
        "RANDOMIZER_MAX": 10,  # Default Value : wait maximum 10s between each email
    }

    return config

# Main app function
def main(config={}) :

    # Config initialisation
    if not config:
        config = init_config()

    # Display loop
    while config["DISPLAY"] == 1 :

        # Router
        match config["ROUTER"]:
            case "login":
                config = login(config)
            case "logout":
                config = logout(config)
            case "email_config":
                config = email_config(config)
            case "set_delivery_list":
                config = set_delivery_list(config)
            case "set_email_subject":
                config = set_subject(config)
            case "set_email_body":
                config = set_body(config)
            case "reset_attachments":
                config = reset_attachments(config)
            case "add_attachment":
                config = new_attachment(config)
            case "server_config":
                config = server_config(config)
            case "set_server_address":
                config = set_server_address(config)
            case "set_port":
                config = set_server_port(config)
            case "set_randomizer":
                config = set_randomizer(config)
            case "start_sending":
                config = auto_mailer(config)
            case _:
                config = main_menu(config)
        main(config)

# Clean the resources dirs from all remaining files before starting the app
clean_dir("email_list/")
clean_dir("email_content/attachments/")
clean_dir("email_content/body/")

# Start the app
main()