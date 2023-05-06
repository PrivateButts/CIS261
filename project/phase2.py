# Randy Butts  CIS261  Project Phase 2


from datetime import datetime


def prompt(p: str) -> str:
    """Prompts for a string"""
    return input(f"{p}: ")

def promptDate(p: str) -> datetime:
    """Prompts for a date in the format MM/DD/YYYY"""
    while True:
        try:
            return datetime.strptime(input(f"{p} (mm/dd/yyyy): "), "%m/%d/%Y")
        except ValueError:
            print("Invalid Date Format. Please use MM/DD/YYYY")
            continue


class Employee:
    name: str
    start_date: datetime
    end_date: datetime
    hours_worked: float
    hourly_rate: float
    income_tax_rate: float

    @property
    def gross_pay(self) -> float:
        return self.hours_worked * self.hourly_rate

    @property
    def income_tax(self) -> float:
        return self.gross_pay * self.income_tax_rate

    @property
    def net_pay(self) -> float:
        return self.gross_pay - self.income_tax

    def __init__(self, name: str):
        self.name = name

    def print(self):
        print(f"Employee Name: {self.name}")
        print(f"From Date: {self.start_date.strftime('%m/%d/%Y')}")
        print(f"End Date: {self.end_date.strftime('%m/%d/%Y')}")
        print(f"Hours Worked: {self.hours_worked}")
        print(f"Hourly Rate: ${self.hourly_rate}/hr")
        print(f"Gross Pay: ${self.gross_pay}")
        print(f"Income Tax Rate: {self.income_tax_rate * 100}%")
        print(f"Income Tax: ${self.income_tax}")
        print(f"Net Pay: ${self.net_pay}")


def addEmployee(name: str) -> Employee:
    e = Employee(name)
    e.start_date = promptDate("Enter Start Date")
    e.end_date = promptDate("Enter End Date")
    e.hours_worked = float(prompt("Enter Hours Worked"))
    e.hourly_rate = float(prompt("Enter Hourly Rate"))
    e.income_tax_rate = float(prompt("Enter Income Tax Rate"))
    return e


def displayTotal(employees: list[Employee]) -> None:
    print("Summery of Employee Information:")
    total_hours, total_gross, total_taxes, total_net = 0, 0, 0, 0

    for e in employees:
        total_hours += e.hours_worked
        total_gross += e.gross_pay
        total_taxes += e.income_tax
        total_net += e.net_pay

    print(f"Total Number of Employees: {len(employees)}")
    print(f"Total Number of Hours: {total_hours}")
    print(f"Total Gross Pay: ${total_gross}")
    print(f"Total Income Taxes: ${total_taxes}")
    print(f"Total Net Pay: ${total_net}")


employees: list[Employee] = []
while True:
    employeeName = prompt("Enter Employee Name or END to exit")

    if employeeName.upper() == "END":
        print()
        print("Employee List:")
        for e in employees:
            e.print()
            print()
        
        displayTotal(employees)
        break
    else:
        employees.append(addEmployee(employeeName))
        print()

    print()
