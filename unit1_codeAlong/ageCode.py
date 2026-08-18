def greet():
    name = input("Enter your name: ")
    print(f"Hello, {name}!")


def get_age():
    age = int(input("Enter your age: "))
    print(f"You are {age} years old.")


def show_message():
    print("Thanks for using this program!")


if __name__ == "__main__":

    greet()
    get_age()
    show_message()
