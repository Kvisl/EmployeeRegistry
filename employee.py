from sqlalchemy.orm import Session
from datetime import datetime, date
from models import Employee

from random import randint,choices
import string
import time


class EmployeeBase:
    def __init__(self, db_session: Session):
        self.db_session = db_session


    def add_employee (self, full_name: str, dob: datetime, gender: str):
        employee = Employee(full_name=full_name, dob=dob, gender=gender)
        self.db_session.add(employee)
        self.db_session.commit()
        self.db_session.refresh(employee)


    def get_all_employees(self):
        employees = self.db_session.query(Employee).order_by(Employee.full_name).all()
        for employee in employees:
            age = datetime.now().year - employee.dob.year
            print(f"{employee.full_name}, {employee.dob}, {employee.gender}, Age: {age}")


    def insert_employee(self, count=1000000):
        def random_name():
            first_letters = list(string.ascii_uppercase)
            first_letter = choices(first_letters, k=1)[0]
            return ' '.join(
                [first_letter + ''.join(choices(string.ascii_lowercase, k=9)) for _ in range(3)]
            )

        def random_gender():
            return choices(['Male', 'Female'], weights=[49, 51])[0]

        def generate_random_birthdate():
            year = randint(1950, 2006)
            month = randint(1, 12)

            if month == 2:
                day = randint(1, 28)
            elif month in [4, 6, 9, 11]:
                day = randint(1, 30)
            else:
                day = randint(1, 31)

            return date(year, month, day)


        employees = []
        for _ in range(count):
            employees.append(
                Employee(full_name=random_name(), dob=generate_random_birthdate(), gender=random_gender())
            )

        for _ in range(100):
            employees.append(
                Employee(full_name=' '.join(['F' + ''.join(choices(string.ascii_lowercase, k=9)) for _ in range(3)]),
                         dob=generate_random_birthdate(), gender='Male')
            )

        self.db_session.bulk_save_objects(employees)
        self.db_session.commit()
        print(f"Добавлено {count + 100} сотрудников.")


    def select_f_male_employees(self):
        start_time = time.time()
        # employees = (self.db_session.query(Employee)
        #              .filter(Employee.gender == 'Male', Employee.full_name.like('F%')).all())
        employees = (
            self.db_session.query(Employee.full_name, Employee.dob, Employee.gender)
            .filter(Employee.gender == 'Male', Employee.full_name.like('F%'))
            .all()
        )


        end_time = time.time()
        with open('query_time_results.txt', 'a', encoding='utf-8') as file:
            file.write(f"Запрос 'select_f_male_employees' выполнен за {end_time - start_time:.4f} секунд.\n")


        count = 0
        for employee in employees:
            count += 1
            print(count)
            print(employee.full_name, employee.dob, employee.gender)

        print(f"Запрос выполнен за {end_time - start_time} секунд.")
