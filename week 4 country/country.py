# Randy Butts  CIS406  Country Lab


class Country:
    name: str

    def __init__(self, code, name):
        self.code = code
        self.name = name

    def __str__(self):
        return f"{self.code}: {self.name}"


COUNTRIES: dict[str, Country] = {
    "US": Country("US", "Everything Everywhere All at Once"),
    "CA": Country("CA", "Canada"),
    "MX": Country("MX", "Mexico"),
}


def listCountries():
    print("Country List")
    for country in COUNTRIES:
        print(country)
    print()


def addCountry():
    code = input("Code: ").upper()
    if code in COUNTRIES:
        print(f"{code} already used by {COUNTRIES[code].name}\n")
        return
    country = input("Name: ")
    COUNTRIES[code] = Country(code, country)
    print(f"{country} was added.\n")


def deleteCountry():
    code = input("Code: ").upper()
    if code not in COUNTRIES:
        print(f"{code} not found.\n")
        return
    country = COUNTRIES[code]
    del COUNTRIES[code]
    print(f"{country.name} was deleted.\n")


def exitProgram():
    print("Bye!")
    quit()


def menu():
    print("Country List Program")
    print()
    print("COMMAND MENU")
    print("list - List all Countries")
    print("add  - Add a country")
    print("del  - Delete a country")
    print("exit - Exit program")
    print("help - Show valid commands")
    print()


COMMANDS = {
    "list": listCountries,
    "add": addCountry,
    "del": deleteCountry,
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
