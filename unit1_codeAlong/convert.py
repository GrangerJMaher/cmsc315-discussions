def miles_to_kilometers(miles):
    return miles * 1.60934


def main():

    miles = float(input("Enter miles: "))

    kilometers = miles_to_kilometers(miles)

    print(f"{miles} miles is {kilometers:.2f} kilometers.")


if __name__ == "__main__":
    main()