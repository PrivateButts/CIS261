# Randy Butts  CIS261  Rectangle


class Rect:
    height: int
    width: int

    def __init__(self, height: int, width: int):
        self.height = height
        self.width = width

    @property
    def perimeter(self):
        return (2 * self.height) + (2 * self.width)

    @property
    def area(self):
        return self.height * self.width

    def display(self):
        print("* " * self.width)
        for i in range(height - 2):
            print("* ", "  " * (self.width - 2), "*", sep="")
        print("* " * self.width)


if __name__ == "__main__":
    while True:
        height = int(input("Height:\t\t"))
        width = int(input("Width:\t\t"))

        rect = Rect(height, width)
        print(f"Perimeter:\t{rect.perimeter}")
        print(f"Area:\t\t{rect.area}")
        rect.display()

        cont = input("\nContinue? (y/n): ")
        if cont.lower() == "n":
            break
