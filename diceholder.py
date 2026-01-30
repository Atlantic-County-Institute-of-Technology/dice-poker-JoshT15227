# diceholder.py
import random
from collections import Counter

dlayer = {

    "top": " ╔═══════════╗ ",
    "blank": " ║           ║ ",
    "pip left": " ║  ●        ║ ",
    "pip center": " ║     ●     ║ ",
    "pip right": " ║        ●  ║ ",
    "two pips": " ║  ●     ●  ║ ",
    "bottom": " ╚═══════════╝ "

}


def display_dice(dice):
    display = ""
    dice_count = len(dice)
    for i in range(dice_count):
        display += dlayer["top"]
    display += "\n"
    for i in range(dice_count):
        match dice[i]:
            case 1:
                display += dlayer["blank"]
            case 2 | 3:
                display += dlayer["pip left"]
            case 4 | 5 | 6:
                display += dlayer["two pips"]
    display += "\n"
    for i in range(dice_count):
        match dice[i]:
            case 1 | 3 | 5:
                display += dlayer["pip center"]
            case 2 | 4:
                display += dlayer["blank"]
            case 6:
                display += dlayer["two pips"]
    display += "\n"
    for i in range(dice_count):
        match dice[i]:
            case 1:
                display += dlayer["blank"]
            case 2 | 3:
                display += dlayer["pip right"]
            case 4 | 5 | 6:
                display += dlayer["two pips"]
    display += "\n"
    for i in range(dice_count):
        display += dlayer["bottom"]
    display += "\n"
    for i in range(dice_count):
        display += f"      [{i + 1}]      "
    return display


class Die:

    def __init__(self):
        self.face = 6
        self.value = random.randint(1, self.face)

    def roll(self):
        self.value = random.randint(1, self.face)
        return self.value

    def get_value(self):
        return self.value


class DiceHandler:
    def __init__(self):
        self.dice = [Die() for _ in range(5)]
        self.keep_list = [False] * 5

    def roll(self):
        results = []
        for i in range(5):
            if not self.keep_list[i]:
                self.dice[i].roll()
            results.append(self.dice[i].get_value())
        return results

    def show(self):
        return [die.get_value() for die in self.dice]

    def keep(self, idx):
        if 0 <= idx < 5:
            self.keep_list[idx] = True

    def unkeep(self, idx):
        if 0 <= idx < 5:
            self.keep_list[idx] = False

    def reset_keeps(self):
        self.keep_list = [False] * 5

    def score(self):
        values = self.show()
        counts = Counter(values)
        freq = sorted(counts.values(), reverse=True)

        if freq == [5]:
            return "Five of a Kind!"
        if freq == [4, 1]:
            return "Four of a Kind!"
        if freq == [3, 2]:
            return "Full House!"
        if freq == [3, 1, 1]:
            return "Three of a Kind!"
        if freq == [2, 2, 1]:
            return "Two Pair!"
        if freq == [2, 1, 1, 1]:
            return "One Pair!"
        if sorted(values) in ([1, 2, 3, 4, 5], [2, 3, 4, 5, 6]):
            return "Straight!"
        return "No Combination"
