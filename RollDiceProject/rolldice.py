import re
from os import system
from random import randint
from functools import reduce


class DiceController(object):
    def __init__(self):
        self.check_roll_input = r'(^roll\s{1})(\d{1,2})(d\d{1,3})(\+\d{1,2})?(\-\d{1,2})?'
        self.check_set_input = r'(^set\s{1})(\d{1,2})'
        self.dice_types = {'d100': 100, 'd50': 50, 'd20': 20, 'd12': 12, 'd10': 10, 'd8': 8, 'd6': 6,
                           'd4': 4, 'd3': 3, 'd2': 2}
        self.test_dc = None

    def roll_dice(self, dice_amount: str, dice_type: str, dice_modifiers: list):
        roll_max_value = self.dice_types[dice_type]
        independent_rolls = []
        for _ in range(int(dice_amount)):
            independent_rolls.append(randint(1, roll_max_value))
        positive_mod, negative_mod = dice_modifiers
        modifiers = [0, 0]
        if dice_modifiers is not [None, None]:
            modifiers[0] = int(positive_mod) if positive_mod is not None else 0
            modifiers[1] = int(negative_mod) if negative_mod is not None else 0
        rolled = reduce(lambda x, y: x + y, independent_rolls)
        modifiers_sum = reduce(lambda x, y: x + y, modifiers)
        result = rolled + modifiers_sum
        print("Roll:", rolled, "\nModifiers:", modifiers_sum, "\nSum:", result)
        if self.test_dc is None:
            return None
        if result < self.test_dc:
            return print(f"You failed the test! The DC was {self.test_dc}")
        return print(f"You passed the test! The DC was {self.test_dc}")

    def set_test_difficulty_class(self, dc):
        self.test_dc = int(dc)
        print(f"The test class difficulty was set to {self.test_dc}")

    def validate_user_input(self, user_input: str):
        if user_input == 'clear':
            system('cls')
            return True
        match = re.search(self.check_set_input, user_input)
        if match:
            self.set_test_difficulty_class(match.group(2))
            return True
        match = re.search(self.check_roll_input, user_input)
        if match:
            if match.group(3) not in self.dice_types.keys():
                return False
            self.roll_dice(match.group(2), match.group(3), [match.group(4), match.group(5)])
            return True
        return False
