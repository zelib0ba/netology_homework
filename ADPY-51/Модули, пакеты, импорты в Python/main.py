import datetime
from application.salary import calculate_salary
from application.db.people import get_employees
if __name__ == '__main__':
    get_employees()
    calculate_salary()
    # печать даты
    now = datetime.datetime.now()
    print (now.strftime("%d-%m-%Y"))

