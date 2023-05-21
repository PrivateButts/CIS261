# Randy Butts  CIS261  Project Phase 3

import json
from datetime import datetime
from typing import Tuple, Union


def prompt(p: str) -> str:
    """Prompts for a string"""
    return input(f"{p}: ")


def promptDate(
    p: str, extra_valid: list[str] = None
) -> Tuple[Union[datetime, str], bool]:
    """Prompts for a date in the format YYYY-MM-DD"""
    while True:
        try:
            i = input(f"{p} (YYYY-MM-DD): ")
            if extra_valid and i.upper() in extra_valid:
                return i, True
            return datetime.strptime(i, "%Y-%m-%d"), False
        except ValueError:
            print("Invalid Date Format. Please use YYYY-MM-DD")
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

    def as_dict(self) -> dict:
        return {
            "name": self.name,
            "start_date": self.start_date.isoformat(),
            "end_date": self.end_date.isoformat(),
            "hours_worked": self.hours_worked,
            "hourly_rate": self.hourly_rate,
            "income_tax_rate": self.income_tax_rate,
        }

    def __init__(self, name: str, **kwargs):
        self.name = name
        for k, v in kwargs.items():
            setattr(self, k, v)

    def print(self):
        print(f"Employee Name: {self.name}")
        print(f"From Date: {self.start_date.strftime('%Y-%m-%d')}")
        print(f"End Date: {self.end_date.strftime('%Y-%m-%d')}")
        print(f"Hours Worked: {self.hours_worked:,.0f}")
        print(f"Hourly Rate: ${self.hourly_rate:,.2f}/hr")
        print(f"Gross Pay: ${self.gross_pay:,.2f}")
        print(f"Income Tax Rate: {self.income_tax_rate * 100}%")
        print(f"Income Tax: ${self.income_tax:,.2f}")
        print(f"Net Pay: ${self.net_pay:,.2f}")


def loadEmployees() -> list[Employee]:
    with open("employees.json", "r") as f:
        json_data = json.load(f)

    employees = []
    for e in json_data:
        e["start_date"] = datetime.fromisoformat(e["start_date"])
        e["end_date"] = datetime.fromisoformat(e["end_date"])
        employees.append(Employee(**e))

    return employees


def saveEmployees(employees: list[Employee]) -> None:
    with open("employees.json", "w") as f:
        json.dump([e.as_dict() for e in employees], f)


def addEmployee(name: str) -> Employee:
    e = Employee(name)
    e.start_date = promptDate("Enter Start Date")[0]
    invalidEndDate = True
    while invalidEndDate:
        e.end_date = promptDate("Enter End Date")[0]
        if e.end_date < e.start_date:
            print("End date must be after start date")
        else:
            invalidEndDate = False
    e.hours_worked = float(prompt("Enter Hours Worked"))
    e.hourly_rate = float(prompt("Enter Hourly Rate"))
    e.income_tax_rate = float(prompt("Enter Income Tax Rate"))
    return e


def displayReport(employees: list[Employee]) -> None:
    print("Report of Employee Information:")
    total_hours, total_gross, total_taxes, total_net = 0, 0, 0, 0

    for e in employees:
        total_hours += e.hours_worked
        total_gross += e.gross_pay
        total_taxes += e.income_tax
        total_net += e.net_pay
        print("*" * 40)
        e.print()
        print("*" * 40, "\n")

    print(f"Total Number of Employees: {len(employees):,}")
    print(f"Total Number of Hours: {total_hours:,}".rstrip(".0"))
    print(f"Total Gross Pay: ${total_gross:,.2f}")
    print(f"Total Income Taxes: ${total_taxes:,.2f}")
    print(f"Total Net Pay: ${total_net:,.2f}")


employees: list[Employee] = []
try:
    employees = loadEmployees()
except FileNotFoundError:
    pass

while True:
    employeeName = prompt("Enter Employee Name or END to exit")

    if employeeName.upper() == "END":
        print()
        reportStart, isAll = promptDate(
            "Enter 'all' for to report all data or enter start date for report",
            extra_valid=["ALL"],
        )

        if isAll:
            reportEmployees = employees
        else:
            reportEmployees = [e for e in employees if e.start_date >= reportStart]

        displayReport(reportEmployees)
        break
    else:
        employees.append(addEmployee(employeeName))
        saveEmployees(employees)
        print()

    print()
