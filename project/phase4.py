# Randy Butts  CIS261  Project Phase 4

from dataclasses import asdict, dataclass
import json
from datetime import datetime
from typing import Tuple, Union


def prompt(p: str, valid_input: list[str] = []) -> str:
    """Prompts for a string"""
    question = p
    if valid_input:
        question += f" ({'/'.join(valid_input)})"
        valid_input = [v.upper() for v in valid_input]
    question += ": "
    while True:
        i = input(question)
        if i.upper() in valid_input or len(valid_input) == 0:
            break
    return i


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


@dataclass
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

    def printHeader(self):
        print(
            "\t".join(
                [
                    "From Date",
                    "End Date",
                    "Name",
                    "Hours Worked",
                    "Hourly Rate",
                    "Gross Pay",
                    "Income Tax Rate",
                    "Income Tax",
                    "Net Pay",
                ]
            )
        )

    def printRow(self):
        print(
            "\t".join(
                [
                    f"{self.start_date.strftime('%Y-%m-%d')}",
                    f"{self.end_date.strftime('%Y-%m-%d')}",
                    f"{self.name}",
                    f"{self.hours_worked:,.0f}\t",
                    f"${self.hourly_rate:,.2f}/hr",
                    f"${self.gross_pay:,.2f}\t",
                    f"{self.income_tax_rate * 100}%\t",
                    f"${self.income_tax:,.2f}\t",
                    f"${self.net_pay:,.2f}",
                ]
            )
        )


def loadEmployees() -> list[Employee]:
    with open("employees.json", "r") as f:
        try:
            json_data = json.load(f)
        except json.JSONDecodeError:
            json_data = []

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
    start_date = promptDate("Enter Start Date")[0]
    invalidEndDate = True
    while invalidEndDate:
        end_date = promptDate("Enter End Date")[0]
        if end_date < start_date:
            print("End date must be after start date")
        else:
            invalidEndDate = False
    hours_worked = float(prompt("Enter Hours Worked"))
    hourly_rate = float(prompt("Enter Hourly Rate"))
    income_tax_rate = float(prompt("Enter Income Tax Rate"))
    return Employee(
        name=name,
        start_date=start_date,
        end_date=end_date,
        hours_worked=hours_worked,
        hourly_rate=hourly_rate,
        income_tax_rate=income_tax_rate,
    )


def displayReport(employees: list[Employee]) -> None:
    print("Report of Employee Information:")
    total_hours, total_gross, total_taxes, total_net = 0, 0, 0, 0

    employees[0].printHeader()
    for e in employees:
        total_hours += e.hours_worked
        total_gross += e.gross_pay
        total_taxes += e.income_tax
        total_net += e.net_pay
        e.printRow()

    print(f"\nTotal Number of Employees: {len(employees):,}")
    print(f"Total Number of Hours: {total_hours:,}".rstrip(".0"))
    print(f"Total Gross Pay: ${total_gross:,.2f}")
    print(f"Total Income Taxes: ${total_taxes:,.2f}")
    print(f"Total Net Pay: ${total_net:,.2f}")


ROLES = ["ADMIN", "USER"]


@dataclass
class User:
    username: str
    password: str
    role: str

    def print(self):
        print(
            f"Username: {self.username}\tPassword: {self.password}\tRole: {self.role}"
        )


def loadUsers() -> dict[str, User]:
    with open("users.json", "r") as f:
        try:
            json_data = json.load(f)
        except json.JSONDecodeError:
            json_data = []

    users = {}
    for u in json_data:
        users[u["username"]] = User(**u)

    return users


def saveUsers(users: dict[str, User]) -> None:
    with open("users.json", "w") as f:
        json.dump([asdict(u) for u in users.values()], f)


users: dict[str, User] = {}
try:
    users = loadUsers()
except FileNotFoundError:
    pass

print("##### Create users, passwords, and roles #####")
while True:
    username = prompt("Enter username or 'End' to quit")
    if username.upper() == "END":
        for u in users.values():
            u.print()
        break
    user = User(
        username=username,
        password=prompt("Enter password"),
        role=prompt("Enter role", valid_input=ROLES).upper(),
    )
    users[username] = user
    saveUsers(users)


employees: list[Employee] = []
try:
    employees = loadEmployees()
except FileNotFoundError:
    pass

print("\n##### Data Entry #####")
username = prompt("Enter username")
password = prompt("Enter password")

valid = False
if username in users.keys():
    valid = users[username].password == password

if not valid:
    print(f"{username} is invalid.")
    exit(0)

user = users[username]


# Add Employees
if user.role == "ADMIN":
    while True:
        employeeName = prompt("Enter Employee Name or END to exit")

        if employeeName.upper() == "END":
            break
        else:
            employees.append(addEmployee(employeeName))
            saveEmployees(employees)
            print()

        print()


# Reporting
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
