import sys
from database import Connector
from employee import EmployeeBase
from datetime import datetime


class Application:
    def __init__(self):
        self.db_connector = Connector()
        self.db_session = self.db_connector.create_session()
        self.repository = EmployeeBase(self.db_session)


    def run(self):
        if len(sys.argv) > 1:
            mode = sys.argv[1]

            if mode == '1':
                self.db_connector.create_tables()



            elif mode == '2':
                full_name = sys.argv[2]
                birth_date = sys.argv[3]
                gender = sys.argv[4]
                birth_date_obj = datetime.strptime(birth_date, "%Y-%m-%d")
                self.repository.add_employee(full_name, birth_date_obj, gender)


            elif mode == '3':
                self.repository.get_all_employees()


            elif mode == '4':
                self.repository.insert_employee()


            elif mode == '5':
                self.repository.select_f_male_employees()


        self.db_session.close()


if __name__ == "__main__":
    app = Application()
    app.run()
