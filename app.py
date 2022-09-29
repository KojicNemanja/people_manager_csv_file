import os
import options
from people_file import PeopleFile
from person_model import Person


file_path = os.getenv("PYTHON_RESOURCES") + "/people_manager_csv/data.csv"
people_file = PeopleFile(file_path)
people_file.load_data()

options.title()
while True:
    answ = options.get_answer()
    if answ == '0':
        options.show_options()
    elif answ == '1':
        people_file.show_all()
    elif answ == '2':
        people_file.add()
    elif answ == '3':
        people_file.edit()
    elif answ == '4':
        people_file.delete()
    elif answ == '5':
        people_file.search()
    elif answ == 'q':
        print("Bye!")
        break
    else:
        print("Please eneter correct option!")
