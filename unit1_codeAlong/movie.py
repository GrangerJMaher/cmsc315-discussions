class Movie:

    def __init__(self, title, rating):
        self.title = title
        self.rating = rating

    def display(self):
        print(f"Title: {self.title}")
        print(f"Rating: {self.rating}")


def main():

    movie1 = Movie("The Adventure", "PG")
    movie2 = Movie("Mystery Island", "PG-13")

    movie1.display()
    print()

    movie2.display()

if __name__ == "__main__":
    main()