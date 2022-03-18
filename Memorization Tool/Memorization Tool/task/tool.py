import sys
flashcards = {}


def add_flashcard():
    q = input("Question:\n")
    while not q.strip("\n "):
        q = input("Question:\n")
    a = input("Answer:\n")
    while not a.strip("\n "):
        a = input("Answer:\n")
    flashcards[q] = a


def add_sub_menu():
    while True:
        print("1. Add a new flashcard")
        print("2. Exit")
        while True:
            option = input()
            if option == '':
                continue
            elif option == '1':
                add_flashcard()
                break
            elif option == '2':
                return
            else:
                print(f"{option} is not an option")
                break


def practice():
    if not flashcards:
        print("There is no flashcard to practice!")
        return
    for card in flashcards:
        print(f"Question: {card}")
        print('Please press "y" to see the answer or press "n" to skip:')
        option = input()
        if option == 'y':
            print(f"Answer: {flashcards[card]}")


def main_menu():
    while True:
        print("1. Add flashcards")
        print("2. Practice flashcards")
        print("3. Exit")
        while True:
            option = input()
            if option == '':
                continue
            elif option == '1':
                add_sub_menu()
            elif option == '2':
                practice()
            elif option == '3':
                print("Bye!")
                sys.exit()
            else:
                print(f"{option} is not an option")
            break


if __name__ == "__main__":
    while True:
        main_menu()


