def encode(input):  # Encode Function added by Tyler
    new_string = ""
    for i in input:
        if int(i) < 7:
            new_string += str(int(i)+3)
        elif i == "7":
            new_string += "0"
        elif i == "8":
            new_string += "1"
        elif i == "9":
            new_string += "2"
    return new_string


# Add def decode here


if __name__ == "__main__":  # Main function added by Tyler
    stored_password = None
    while True:
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n")
        menu_select = input("Please enter an option: ")
        if menu_select == "1":
            user_input = input("Please enter your password to encode: ")
            stored_password = encode(user_input)
            print("Your password has been encoded and stored")
            print()
        elif menu_select == "2":
            print(f"The encoded password is {stored_password}, and the original password is {decode(stored_password)}")
            print()
        elif menu_select == "3":
            break
