import os
import random
import socket
import time
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from src.display.print_colors.PrintColors import PrintColors
from src.services.file_service.file_service import clean_dir

# Check internet connexion
def network_check():

    # Try to connect to the DNS
    try:
        # Set default timeout to 2 seconds
        socket.setdefaulttimeout(2)
        # Connection to 8.8.8.8:53 (DNS)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect(("8.8.8.8", 53))
        # If no error occur, internet connexion is OK
        return True
    # If an error occur, then no internet connexion
    except OSError:
        return False

# Check that all necessary configuration is set
def check_config(config):

    # Check login
    if not (config["USER_EMAIL"] and config["USER_PASSWORD"]):
        print(PrintColors.RED + "Unable to start the mailer : Login Required" + PrintColors.END)
        # Return to the menu
        config["ROUTER"] = ""
        return config

    # Check email list file
    if not os.path.exists("email_list/email_list.txt"):
        print(PrintColors.RED + "Unable to start the mailer : Email List Required" + PrintColors.END)
        # Return to the menu
        config["ROUTER"] = ""
        return config

    # Check email content file
    if not (os.path.exists("email_content/body/body.txt") and config["SUBJECT"]):
        print(PrintColors.RED + "Unable to start the mailer : Email List Required" + PrintColors.END)
        # Return to the menu
        config["ROUTER"] = ""
        return config

    # Check that no attachments listed in the config are missing
    for attachments in config["ATTACHMENTS"]:
        if not os.path.exists("email_content/attachments/" + attachments):
            print(PrintColors.RED + "An error occurred with the attachments, please reload the attachments and retry" + PrintColors.END)
            clean_dir("email_content/attachments/")
            # Return to the menu
            config["ROUTER"] = ""
            return config

    # Check internet connexion
    if not network_check():
        print(PrintColors.RED + "Unable to start the mailer : Internet Connexion is required" + PrintColors.END)
        # Return to the menu
        config["ROUTER"] = ""
        return config

    # If the configuration is alright, redirection to the mail sender
    config["ROUTER"] = "start_sending"
    return config

# Load attachments file to be inserted into the email
def load_attachments():

    # Loaded attachments list initialisation
    loaded_attachments = []
    # List all files into the attachment storage repository
    attachments = [f for f in os.listdir("email_content/attachments/") if os.path.isfile(os.path.join("email_content/attachments/", f))]

    # For each file in the storage repository...
    for file in attachments:

        # Open and encode the file into email format
        with open("email_content/attachments/" + file, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header(
                "Content-Disposition",
                f"attachment; filename={file}",
            )
            loaded_attachments.append(part)
            # Reset variable to avoid conflicts
            part = None

    # Return all the loaded attachments
    return loaded_attachments

# Load the content of the mail
def load_body():

    # Try to get the email content from the content storage file
    try :
        with open("email_content/body/body.txt", "r", encoding="utf-8") as txt:
            body = txt.read()

    # If the file is not found, print an error and set an empty body
    except FileNotFoundError:
        body = ""
        print(PrintColors.RED + "Unable to load body" + PrintColors.END)

    # Return the body
    return body

# Correct a problematic line of the email list
def correct_list(counter):

    # Fetch the content of the email list
    with open("email_list/email_list.txt", "r", encoding="latin-1") as f:
        lines = f.readlines()

    # Delete the problematic line
    if counter < len(lines):
        print(f"{PrintColors.RED} Suppression de la ligne {counter + 1} : {lines[counter].strip()} {PrintColors.END}")
        del lines[counter]

        # Rewrite the email list
        with open("email_list/email_list.txt", "w", encoding="latin-1") as f:
            f.writelines(lines)

# Automatic mail sender
def auto_mailer(config,start=0):

    # Counter var is used to remember the nbr of the last treated line in case of an error
    counter = start
    # Get the loaded email attachments
    loaded_attachments = load_attachments()
    # Get the loaded body
    body = load_body()

    # Header
    print(PrintColors.BOLD + "===============================================")
    print(" Starting to send emails " + PrintColors.END)

    # Open the email list and treat every email line by line
    with open("email_list/email_list.txt", "r", encoding="latin-1") as txt:

        # For each email in the list ...
        for email in txt:

            # Error fallback : bypass already treated emails in case of error
            if start:
                start -= 1
                continue
            else:
                # Try to send the configured email to the email address
                try:
                    # Create email
                    message = MIMEMultipart()
                    message['Subject'] = config["SUBJECT"]
                    message['From'] = config["USER_EMAIL"]
                    message['To'] = email.strip()

                    # Attach body
                    email_content = MIMEText(body)
                    message.attach(email_content)

                    # Attach the attachments
                    for attachment in loaded_attachments:
                        message.attach(attachment)

                    # Send the mail
                    with smtplib.SMTP_SSL(config["SERVER"], config["PORT"]) as server:
                        server.login(message['From'], config["USER_PASSWORD"])
                        server.sendmail(message['From'], [email], message.as_string())

                    # Line successfully treated
                    counter += 1
                    # Print confirmation
                    print(f"{PrintColors.GREEN} Sent : {email} {PrintColors.END}")
                    # Start random waiting time
                    time.sleep(random.randint(config["RANDOMIZER_MIN"], config["RANDOMIZER_MAX"]))

                # If an error occurs
                except Exception as e:

                    # Check if the error is related to the internet connexion
                    if network_check(): # If the internet connexion is OK, correct the problematic line in the list
                        # Print error
                        print(f"{PrintColors.RED} Error : {email} - {str(e)} {PrintColors.END}")
                        # Call the email list correction function
                        correct_list(counter)
                        # Resume the function at the following line
                        auto_mailer(start=counter)

                    else : # If there is no internet connexion, stop sending emails
                        # Print error
                        print(PrintColors.RED + "Error : Internet Connexion Lost" + PrintColors.END)
                    # Stop looping in the file
                    break

    # Redirection to the main menu
    config["ROUTER"] = ""
    return config