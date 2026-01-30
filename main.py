# main.py
from diceholder import DiceHandler, display_dice


def get_dice_selection():
    raw = input("Enter dice numbers (1-5) separated by spaces: ")
    try:
        return [int(x) - 1 for x in raw.split() if 1 <= int(x) <= 5]
    except ValueError:
        return []


def play_game():
    handler = DiceHandler()
    rolls = 0
    while rolls < 3:
        rolls += 1
        handler.roll()
        print("\nRoll", rolls)
        print(display_dice(handler.show()))
        if rolls == 3:

            break
        while True:
            print("\nMenu")
            print("1. Keep dice")
            print("2. Un-keep dice")
            print("3. Roll again")
            choice = input("Choose an option: ")
            if choice == "1":
                keep = get_dice_selection()
                for idx in keep:
                    handler.keep(idx)
                print("Dice kept.")
            elif choice == "2":
                unkeep = get_dice_selection()
                for idx in unkeep:
                    handler.unkeep(idx)
                print("Dice un-kept.")
            elif choice == "3":
                break
            else:
                print("Invalid choice.")
    print("\nFinal Dice:")
    print(display_dice(handler.show()))
    print("Result:", handler.score())


def main():
    while True:
        print("\nDice Poker")
        print("1. Start Game")
        print("2. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            play_game()
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


main()
