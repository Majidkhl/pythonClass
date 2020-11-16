
import datetime
import pandas as pd


list_employee_id = []

class Employee:
    """
    A HR class to manage employees database
    """

    def __init__(self, employee_id, first_name, last_name, hire_date):
        self.__employee_id = employee_id   # instance variable unique to each instance
        self.__first_name = first_name
        self.__last_name = last_name
        self.__hire_date = hire_date


        if self.__employee_id in list_employee_id:
            print("Record could not be added")
            sorted_id = sorted(list_employee_id)
            last_id = int(sorted_id[-1])
            print(f"employee_id {self.__employee_id} already exist! "
            f"Please use un employee_id above :{last_id}")
        else:
            list_employee_id.append(self.__employee_id)
            print(f" {self.__first_name} {self.__last_name} added to database! ")

    # employee_id setter, getter
    def set_employee_id(self, employee_id):
        self.__employee_id = employee_id
    def get_employee_id(self):
        return self.__employee_id

    # first_name_id setter, getter
    def set_first_name(self, first_name):
        self.__first_name = first_name
    def get_first_name(self):
        return self.__first_name

    # lats_name_id setter, getter
    def set_last_name(self, last_name):
        self.__last_name = last_name
    def get_last_name(self):
        return self.__last_name

    # hire_date setter, getter
    def set_hire_date(self, hire_date):
        self.__hire_date = hire_date
    def get_hire_date(self):
        return self.__hire_date


    def fullName(self):
        return '{} {}'.format(self.__first_name, self.__last_name)


    def infoEmployee(self):
        print(f"Employee_id: {self.__employee_id}")
        print(f"first_name: {self.__first_name}")
        print(f"last_name: {self.__last_name}")
        format_str = '%d/%m/%y'  # The format
        hire_datetime = datetime.datetime.strptime(self.__hire_date, format_str)
        print(f"hire_date: {hire_datetime.date()}")



    def fire(self):
        list_employee_id.remove(self.__employee_id)
        print(f" {self.__first_name} {self.__last_name} removed from database! ")


    def resign(self, resignation = 'False'):
        if resignation == 'True':
            print(f"Employee {self.__first_name} {self.__last_name} has resigned")

        elif resignation == 'False':
            print(f"Employee {self.__first_name} {self.__last_name} is still employee of the company")


path = 'C:/Users/a_khl/PycharmProjects/dataFrame/venv/Data/'
employees_file = 'employees.csv'

# Creation du employee dataframe
employees_df = pd.read_csv(f"{path}{employees_file}", delimiter=";")

#creating list of employees from employees_dataframe
list_employees = []

counter = 0
for employee in employees_df['EMPLOYEE_ID']:
    if employee != 'EMPLOYEE_ID':
        list_employees.append(Employee(employee,
                                       employees_df['FIRST_NAME'][counter],
                                       employees_df['LAST_NAME'][counter],
                                       employees_df['HIRE_DATE'][counter]))
        counter += 1


def fire_employee(employee_id):
    for item in list_employees:
        if item.get_employee_id() == employee_id:
            print(f"Are you sure you want to fire {item.fullName()}?,")

            counter = 1
            while counter < 4:
                answer = input(f"Type y to confirm or n to cancel:\n")
                if answer.lower() == 'y' or answer.lower() == 'yes':
                    fire_index = (list_employees.index(item))
                    print(fire_index)
                    del list_employees[fire_index]
                    print(f" {item.fullName()} is fired?")
                    break
                elif answer == 'n' or answer.lower() == 'no':
                    print(f"Program cancelled")
                    break
                else:
                    if counter == 3:
                        print("You entered a wrong answer. Program aborted. Please try to rerun the program")
                        break
                    else:
                        counter+=1


# firing employee whose iD == 200
#fire_employee(200)

# emp1 = Employee(300, 'Jim', 'Carey', '12/12/12')
# print(list_employee_id)
# emp1.fire()
# print(emp1.get_employee_id())
# print(list_employee_id)






