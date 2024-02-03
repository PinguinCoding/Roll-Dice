from rolldice import DiceController


def start():
    myDice = DiceController()
    print("Type 'roll <amount><dice type><positive modifier><negative modifier>'\n"
          "Ex: 'roll 1d20+5-2'\n"
          "Type 'set <value>' to set the CD test to a desirable value\n"
          "Type 'clear' to clear the prompt"
          "Type 'quit' to leave")
    while True:
        user_input = str(input("> ")).strip().lower()
        if user_input == 'quit':
            break
        check = myDice.validate_user_input(user_input)
        if user_input == 'clear':
            print("Type 'roll <amount><dice type><positive modifier><negative modifier>'\n"
                  "Ex: 'roll 1d20+5-2'\n"
                  "Type 'set <value> to set the CD test to a desirable value\n"
                  "Type 'quit' to leave.")
        while check is False:
            print("Command Invalid")
            user_input = str(input("> ")).strip().lower()
            if user_input == 'quit':
                break
            check = myDice.validate_user_input(user_input)
            if user_input == 'clear':
                print("Type 'roll <amount><dice type><positive modifier><negative modifier>'\n"
                      "Ex: 'roll 1d20+5-2'\n"
                      "Type 'set <value> to set the CD test to a desirable value\n"
                      "Type 'quit' to leave.")
        if user_input == 'quit':
            break


start()
