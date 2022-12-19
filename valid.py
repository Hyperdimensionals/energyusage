def get_integer(prompt="Please enter an integer: "):
    """
    Function to prompt for and return a valid integer.
    :param prompt: string, Optional string to use as prompt
    :return: integer, Valid integer
    """
    num = 0
    while True:
        try:
            num = int(input(prompt))
            return num
        except:
            print("Invalid integer.")

def get_real(prompt="Please enter an real number: "):
    """
    Function to prompt for and return a valid real number
    :param prompt: string, Optional string to use as prompt
    :return: float, Valid real number
    """
    num = 0.0
    while True:
        try:
            num = float(input(prompt))
            return num
        except:
            print("Invalid number.")

def get_real_positive(prompt="Please enter a positive number: "):
    """
    Function to prompt for and return a valid real number
    :param prompt: string, optional string to use as prompt
    :return: float, Valid real number
    """
    num = 0.0
    while True:
        try:
            num = float(input(prompt))
            if num > 0:
                return num
            else:
                print("Number must be positive.")
        except:
            print("Invalid number.")

def get_string(prompt="Please enter a string: ", str_list=None):
    """
    Function to prompt for and return a string of characters.
    An empty string is invalid input.
    :param prompt: string, Optional string to use as prompt
    :return: string, Non-empty string of characters
    """
    chars = ""
    while True:
        chars = input(prompt)
        duplicates = duplicates_present(chars, str_list) if str_list else False
        if duplicates:
            print("There is already a device with that name, please choose another.")
        elif len(chars) > 19:
            print("Device name too long, please use a shorter name.")
        elif (chars != ""):
            return chars
        else:
            print("Invalid string.")

def duplicates_present(input_str, str_list):
    """
    Function to check for duplicate strings in given list
    :param input_str: string, String to check against
    :param str_list: list, List of strings
    :return:
    """
    if input_str in str_list:
        return True
    else:
        return False
def get_y_or_n(prompt="Please enter 'y' or 'n': "):
    """
    Function to prompt for 'y' or 'n' and return a corresponding bool.
    'Y', 'N', and all cases of 'yes' and 'no' are accepted.
    :param prompt: string, Optional string to use as prompt
    :return: Bool, returns True if yes and False if No
    """
    answer = ""
    answer = input(prompt)
    answer = answer.lower()
    answer_bool = None

    if answer == "y" or answer == "yes":
        answer_bool = True
    elif answer == "n" or answer == "no":
        answer_bool = False
    else:
        print("Please type 'y' or 'n' for Yes or No.")
        answer_bool = get_y_or_n(prompt)

    return answer_bool