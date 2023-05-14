# Randy Butts  CIS261  Invoice Line Calculator


class ContinueOption(str):
    def __new__(cls, value):
        value = value.lower()
        if value not in ("y", "n"):
            raise ValueError(f"Invalid continue option: {value}")
        return super().__new__(cls, value)


def prompt(prompt, t) -> any:
    while True:
        try:
            return t(input(prompt + ": "))
        except ValueError:
            print(f"Invalid {t.__name__}. Please try again.")


if __name__ == "__main__":
    print("The Invoice Line Calculator")

    while True:
        price = prompt("\nEnter price", float)
        quantity = prompt("Enter quantity", int)

        print(f"\nPRICE:    {f'${price:.2f}':>8}")
        print(f"QUANTITY: {quantity:>8}")
        print(f"TOTAL:    {f'${price*quantity:.2f}':>8}\n")

        cont = prompt("Enter another line item? (y/n)", ContinueOption)
        if cont == "n":
            break
    print("Goodbye!")
