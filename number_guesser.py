import random
class NumberGuesser:
    """
    This is the number guesser game's class. A random integer will be
    generated, and the player will have to guess what the integer is based
    on feedback for each answer. The game will keep track of how many
    valid attempts are taken.

    To start the game, players must open a terminal and type the follow 
    command: python -i "number_guesser.py"

    The player must type g = NumberGuesser() to create a game session.

    The player must then type g.diff_select(), and will be prompted
    to type "easy", "medium, or "hard" to select their difficulty option. 
    The player must select a difficulty option before they start a game session.

    To start a game session, the player must type g.game().

    The player will be prompted to type an integer within the range
    (inclusive) defined by the difficulty they chose. If they choose
    something that is not an integer or is outside the defined range,
    they will be prompted with an appropriate message telling them
    to select a valid integer.

    If the player chooses a valid integer, the game will determine if
    it is the correct integer, too high, or too low. The game will
    provide the appropriate feedback, depending on which of the three
    scenarios takes place. The number of attempts only increases when
    the player selects a valid integer. The game will continue until
    the player selects the correct integer.
    """


    # Defines random number generated, number range, difficulty chosen,
    # whether the player's guess is an integer, whether the player
    # guessed correctly, the number of valid tries the player has,
    # and the maximum number of tries the player has.
    def __init__(self):
        self.num = 0
        self.range = ""
        self.diff_chosen = False
        self.is_integer = False
        self.guessed_correct = False
        self.num_tries = 0
        self.max_tries = 20


    # Players input either "easy", "medium", or "hard" to choose their difficulty.
    def diff_select(self):
        selection = input("Select a difficulty: easy, medium, or hard: ")
        while selection != "easy" and selection != "medium" and selection != "hard":
            selection = input("Invalid selection. Choose easy, medium, or hard: ")
        if selection == "easy":
            self.range = "1-100"
            self.num = random.randint(1, 100)
            self.diff_chosen = True
            return "You have selected easy!"
        elif selection == "medium":
            self.range = "1-150"
            self.num = random.randint(1, 150)
            self.diff_chosen = True
            return "You have selected medium!"
        elif selection == "hard":
            self.range = "1-200"
            self.num = random.randint(1, 200)
            self.diff_chosen = True
            return "You have selected hard!"


    # Each player input must be an integer within the range. Each valid input will be
    # interpreted as correct, too high, or too low, and will yield the appropriate feedback.
    def game(self):
        while self.diff_chosen is False:
            return "Please select your difficulty before starting a game session."
        
        # Determines if the input is an integer.
        while self.guessed_correct is False:
            while self.is_integer is False:
                char_checker = []
                num_guessed = input(f"Choose an integer between {self.range}: ")
                if num_guessed[0] not in "-0123456789":
                    print(f"Input must be an integer between {self.range}")
                else:
                    char_checker.append(num_guessed[0])
                    for char in num_guessed[1:]:
                        if char not in "0123456789":
                            print(f"Input must be an integer between {self.range}")
                        else:
                            char_checker.append(char)
                char_checker = "".join(char_checker)
                if char_checker == num_guessed:
                    self.is_integer = True

            if self.is_integer is True:
                num_guessed = int(num_guessed)
                # Returns a message if the integer is out of range.
                if self.range == "1-100" and num_guessed > 100:
                    self.is_integer = False
                    print("Integer must be 100 or less.")
                elif self.range == "1-150" and num_guessed > 150:
                    self.is_integer = False
                    print("Integer must be 150 or less.")
                elif self.range == "1-200" and num_guessed > 200:
                    self.is_integer = False
                    print("Integer must be 200 or less.")
                elif num_guessed < 1:
                    self.is_integer = False
                    print("Integer must be 1 or more.")

                # Determines if the valid integer is correct, too high, or too low.
                # Prints number of tries and max tries allowed.
                else:
                    if num_guessed == self.num:
                        self.guessed_correct = True
                    elif num_guessed > self.num:
                        self.is_integer = False
                        print("Guess lower!")
                    elif num_guessed < self.num:
                        self.is_integer = False
                        print("Guess higher!")
                    self.num_tries += 1
                    print(f"Number of tries: {self.num_tries}. Max tries: {self.max_tries}")
                    if self.num_tries == self.max_tries:
                        return f"Game over! The correct number was: {self.num}"
        return f"Congratulations! You guessed correctly! The correct number was: {self.num}. Total tries: {self.num_tries}"
