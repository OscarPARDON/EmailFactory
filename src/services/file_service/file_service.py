import os

# Clean a repository from all its files
def clean_dir(directory):

    # For all the files detected in the repository
    for file in os.listdir(directory):
        path = os.path.join(directory, file)

        # Remove the file
        if os.path.isfile(path):
            os.remove(path)

# Clean all the resources repository
def clean_all_dirs():

    # Clean the email list storage repository
    clean_dir("email_list/")
    # Clean the attachments storage repository
    clean_dir("email_content/attachments/")
    # Clean the body storage repository
    clean_dir("email_content/body/")