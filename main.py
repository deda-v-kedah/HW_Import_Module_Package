from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import datetime
import matplotlib.pyplot as plt


def create_gr():
    plt.plot([1, 2, 3, 4, 5], [1, 2, 3, 4, 5])
    plt.show()  

def date_now():
    date = datetime.now()
    print( f"{date.year}-{date.month}-{date.day}" )



def main():

    date_now()

    calculate_salary()
    get_employees()

    create_gr()


if __name__ == '__main__':
    main()