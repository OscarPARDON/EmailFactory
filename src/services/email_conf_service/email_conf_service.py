import os
import re
import shutil
import subprocess
from src.display.print_colors.PrintColors import PrintColors
from src.services.file_service.file_service import clean_dir

# This function enable to configure the subject of the mail
def set_subject(config):

    # Header
    print(PrintColors.BOLD + "=================================")
    print(" Your email subject " + PrintColors.END)

    # Ask the user for a subject
    subject = input(" Enter your email subject : ")

    # If the subject is not empty : add it in the configuration
    if subject:
        config["SUBJECT"] = subject
    else : # If the given subject is empty, raise a validation error
        print(PrintColors.RED + "ValidationError : The subject can not be empty ! " + PrintColors.END)

    # Redirection to the email configuration menu
    config["ROUTER"] = "email_config"
    return config

# Import the email content from a txt file
def import_email_body(config):

    # If content is already loaded : ask the user permission to replace it
    if config["GET_BODY"]:
        check = input("A body is already loaded, do you want to replace it ? [y/n] : ")
    else:
        check = "y"

    # If the user wants to load or replace content
    if check == "y":

        # Clean the directory beforehand and reset the config boolean to avoid errors
        clean_dir("email_content/body/")
        config["GET_BODY"] = 0

        # Ask the user for the path to the txt file that contains the mail content
        path = input("Please enter the absolute path of the txt file : ")

        # Regex that verify that the user input is a path that leads to a txt file
        PATH_REGEX = re.compile(r"^/.*\.txt$")

        # If the path is valid, load the file into the designated directory
        if path and PATH_REGEX.match(path):
            # Try to copy the file in the designated directory
            try:
                shutil.copy(path, "email_content/body/body.txt")
                # Inform the config that a body has been loaded
                config["GET_BODY"] = 1
                # Confirm the success
                print(PrintColors.GREEN + "Content successfully loaded ! " + PrintColors.END)

            # Error Handling
            except Exception as e:
                print(PrintColors.RED + e + PrintColors.END)

        else:  # If the path is invalid, raise a validation error
            print(PrintColors.RED + "A valid absolute path to a txt file is mandatory ! " + PrintColors.END)

    return config

# Add / Edit email content with text editor
def edit_email_body(config):

    # Try to open the email content file in the editor
    try:
        # Get the default text editor of the user
        editor = os.environ.get("EDITOR") or os.environ.get("VISUAL") or "nano"
        # Open the email content file in the editor
        subprocess.run([editor, "email_content/body/body.txt"])
        # Inform the config that a body has been loaded
        config["GET_BODY"] = 1

        # Confirmation message
        print(PrintColors.GREEN + "Content successfully edited ! " + PrintColors.END)

    # Error Handling
    except Exception as e:
        print(PrintColors.RED + e + PrintColors.END)

    return config

# Set the email content (body)
def set_body(config):

    # Header
    print(PrintColors.BOLD + "=================================")
    print(" Your email content " + PrintColors.END)

    # Ask the user : import content via txt file or open editor
    choice = input("Import a txt file [1] or open editor [2] ? : ")

    match choice:
        case "1": # Import via txt file
            import_email_body(config)
        case _: # Open editor
            edit_email_body(config)

    # Redirection to the email configuration menu
    config["ROUTER"] = "email_config"
    return config

# Add an attachment to the email
def new_attachment(config):

    # Header
    print(PrintColors.BOLD + "=================================")
    print(" Add a new attachment " + PrintColors.END)

    # Ask the user for an absolute file to the txt file
    path = input("Please enter the absolute path of the file : ")

    # Validate that the path is an absolute file
    if path and path[0] == "/":

        # Try to copy the file at the given path
        try:
            # Get the filename of the file
            filename = os.path.basename(path)
            # Copy the file into the attachment storage repository, and keep the same filename
            shutil.copy(path, "email_content/attachments/" + filename)
            # Add the attachment filename to the attachments list in the configuration
            config["ATTACHMENTS"].append(filename)

            # Confirmation message
            print(PrintColors.GREEN + "Attachment successfully added !" + PrintColors.END)

        # Error Handling
        except Exception as e:
            print(PrintColors.RED + e + PrintColors.END)

    else: # If the path is not valid, raise a validation error
        print(PrintColors.RED + "A valid absolute path is mandatory ! " + PrintColors.END)

    # Redirection to the configuration menu
    config["ROUTER"] = "email_config"
    return config

# Reset the attachments
def reset_attachments(config):

    # Clean attachment repository from all residual files
    clean_dir("email_content/attachments/")
    # Reset the attachment list in the config
    config["ATTACHMENTS"] = []
    # Confirmation message
    print(PrintColors.GREEN + "Attachments successfully reset ! " + PrintColors.END)

    # Redirection to the email configuration menu
    config["ROUTER"] = "email_config"
    return config
