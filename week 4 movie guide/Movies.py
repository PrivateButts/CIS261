# Randy Butts  CIS261  Movie Guide Lab


MOVIES: list[str] = [
    "Everything Everywhere All at Once",
    "Isle of Dog",
    "The Grand Budapest Hotel",
]


def listMovies():
    for i, movie in enumerate(MOVIES, start=1):
        print(f"{i}. {movie}")
    print()


def addMovie():
    movie = input("Title: ")
    MOVIES.append(movie)
    print(f"{movie} was added.\n")


def deleteMovie():
    index = int(input("Number: "))
    if index < 1 or index > len(MOVIES):
        print("Invalid movie number.\n")
        return
    movie = MOVIES.pop(index - 1)
    print(f"{movie} was deleted.\n")


def exitProgram():
    print("Bye!")
    quit()


def menu():
    print("Movie List Program")
    print()
    print("COMMAND MENU")
    print("list - List all movies")
    print("add  - Add a movie")
    print("del  - Delete a movie")
    print("exit - Exit program")
    print("help - Show valid commands")
    print()


COMMANDS = {
    "list": listMovies,
    "add": addMovie,
    "del": deleteMovie,
    "exit": exitProgram,
    "help": menu,
}


if __name__ == "__main__":
    menu()
    while True:
        command = input("Command: ").lower()
        if command in COMMANDS:
            COMMANDS[command]()
        else:
            print("Not a valid command. Please try again.\n")
