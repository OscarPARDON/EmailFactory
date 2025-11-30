from src.display.print_colors.PrintColors import PrintColors

# Set the SMTP server address
def set_server_address(config):

    # Header
    print(PrintColors.BOLD + "======================================")
    print("Changing server address" + PrintColors.END)

    # User Input : SMTP server address (example : smtp.google.com)
    address = input("Enter server address: ")

    # If the address is validated, add it to the configuration
    if address :
        config["SERVER"] = address
    else : # If the address is empty, raise a validation error
        print(PrintColors.RED + "ValidationError : A server address is required !" + PrintColors.END)

    # Redirection to the server configuration menu
    config["ROUTER"] = "server_config"
    return config

# Set the port used to send mail
def set_server_port(config):

    # Header
    print(PrintColors.BOLD + "======================================")
    print("Changing server port" + PrintColors.END)

    # User input : Mailing Server Port
    port = input("Enter a port number : ")

    # If the port is validated, add it to the config
    if port and port.isnumeric():
        config["PORT"] = port
    else: # If the port is not validated, raise an error
        print(PrintColors.RED + "ValidationError : A port is required !" + PrintColors.END)

    # Redirection to the server configuration menu
    config["ROUTER"] = "server_config"
    return config

# Set waiting time range
def set_randomizer(config):

    # Header
    print(PrintColors.BOLD + "======================================")
    print("Changing randomizer" + PrintColors.END)

    # User input : Minimum waiting time in seconds
    min_rand = input("Minimum sleeping time (s) : ")
    # User input : Maximum waiting time in seconds
    max_rand = input("Maximum sleeping time (s) : ")

    # Initialisation of validation variables
    check = 1
    error = ""

    # Minimum waiting time validation
    if not (min_rand and min_rand.isnumeric() and int(min_rand) > 0) :
        check = 0
        error = PrintColors.RED + "ValidationError : A number of second is required !" + PrintColors.END

    # Maximum waiting time validation
    if not (max_rand and max_rand.isnumeric() and int(max_rand) > 0) :
        check = 0
        error = PrintColors.RED + "ValidationError : A number of second is required !" + PrintColors.END

    # Check that the minimum waiting time is lower than the maximum waiting time
    if check and min_rand < max_rand :
        check = 0
        error = PrintColors.RED + "ValidationError : Maximum sleeping time can not be less than minimum sleeping time !" + PrintColors.END

    # If the validation fails, print the error
    if not check :
        print(error)
    else : # If the data is validated, update the configuration
        config["RANDOMIZER_MIN"] = min_rand
        config["RANDOMIZER_MAX"] = max_rand

    # Redirection to the server configuration menu
    config["ROUTER"] = "server_config"
    return config