from cgi import test
import csv
from person_model import Person

class PeopleFile:
    def __init__(self, path):
        self.path = path
        self.changes = True
        self.people = []

    def load_data(self):
        if self.changes:
            print("Read csv...")
            self.people.clear()
            with open(self.path, "r") as f:
                csv_reader = csv.DictReader(f)
                for row in csv_reader:
                    self.people.append(Person.from_row(row))
                self.changes = False
        return self.people


    def show_all(self):
        if not self.is_empty():
            print("---> SHOWING PERSON <---")
            people = self.load_data()
            self.read_list(people)
            """print("{:<5}{:<15}{:<20}".format("id", "First name", "Last name"))
            for person in people:
                print(person)"""

    def read_list(self, data):
        print("{:<5}{:<15}{:<20}".format("ID", "First name", "Last name"))
        for person in data:
            print(person)

    
    def get(self, persons_id: int):
        people = self.load_data()
        if people is not None:
            for person in people:
                if int(person.id) == int(persons_id):
                    return person
        return None

    def get_for_phrase(self, phrase:str):
        people = self.load_data()
        filtered_people = []
        phrase = phrase.strip().casefold()# remove whitespace and transform in lower case
        for person in people:
            join_data = str(person.id + person.f_name + person.l_name).casefold()
            result = str(join_data).find(phrase)
            if result > -1:
                filtered_people.append(person)
        return filtered_people

    def add(self):
        print("---> ADDING PERSON <---")
        try:
            people = self.load_data()
            new_person = Person(
                int(input("Enter id: ").strip()),
                input("Eneter first name: ").strip(),
                input("Enter last name: ").strip()
            )
            if self.is_data_valid(new_person):
                people.append(new_person)
                result = self.write_to_file(people)
                if result > 0:
                    print("New person is successful added!")
                else:
                    print("Soomething is wrong!")
        except ValueError as ex:
            print(ex)

    def edit(self):
        if not self.is_empty():
            print("---> EDITING PERSON <---")
            try:
                id = int(input("Enter person's ID: "))
                person = self.get(id)
                if person is not None:
                    self.show_persons_data(person)
                    new_person = person
                    answ = input("Do you want to edit First name? (y/n): ")
                    if answ == 'y':
                        first_name = input("Enter a new First name: ")
                        new_person.f_name = first_name
                    answ = input("Do you want to edit Last name? (y/n): ")
                    if answ == 'y':
                        last_name = input("Enter a new Last name: ")
                        new_person.l_name = last_name
                    self.show_persons_data(new_person)
                    answ = input("Do you want to save changes? (y/n): ")
                    if answ == 'y':
                        people = self.load_data()
                        for person in people:
                            if int(person.id) == int(id):
                                person = new_person
                                break
                        result = int(self.write_to_file(people))
                        if result == 1:
                            print("Data is changed!")
                        else:
                            print("Somethin is worng!")
                    else:
                        print("Changes discard!")
                else:
                    print("Person with entered ID is not exists!")
            except ValueError as ex:
                print(ex)
        
    def delete(self):
        if not self.is_empty():
            print("---> DELETING PERSON <---")
            try:
                id = int(input("Enter persons ID: "))
                person = self.get(id)
                if person is not None:
                    print("***  Person's data  ***")
                    print("ID: ", person.id)
                    print("First name: ", person.f_name)
                    print("Last name: ", person.l_name)
                    answ = input("Do you wish to delete person (y/n): ")
                    if answ == 'y':
                        if self.commit_delete(person) > 0:
                            print("Person was successful delete")
                        else:
                            print("Something is wrong!")
                else:
                    print("Person with entered ID is not exists!")
            except ValueError as ex:
                print(ex)

    
    def search(self):
        if not self.is_empty():
            print("---> SEARCHING PERSONS <---")
            phrase = input("Enter some data of person \n(id, first name, last name): ")
            people = self.get_for_phrase(phrase)
            self.read_list(people)

    def commit_delete(self, person):
        persons_id = person.id
        people = self.people
        for p in people:
            if int(p.id) == int(persons_id):
                self.people.remove(p)
                return self.write_to_file(people)
        return 0

    def write_to_file(self, people):
        header = ["id","first_name","last_name"]
        try:
            with open(self.path, "w", newline="") as f:
                csv_writer = csv.DictWriter(f, fieldnames=header, delimiter=",")
                csv_writer.writeheader()
                for person in people:
                    csv_writer.writerows(person.to_write_row())
                self.changes = True
                return 1
        except Exception as ex:
            print(ex)
            return 0

    def is_empty(self):
        size = len(self.people)
        if size < 1:
            print("List of people is empty!")
            return True
        return False

    def show_persons_data(self, person):
        print("---> Person's data <---")
        print("ID: ", person.id)
        print("First name: ", person.f_name)
        print("Last name: ", person.l_name)

    def is_data_valid(self, new_person):
        if new_person.id == "":
            print("Person's ID is empty!")
            return False
        if self.is_exists(new_person.id):
            print("Person with ID: {}, alredy exists!".format(new_person.id))
            return False
        if new_person.f_name == "":
            print("Fisrt name is empty!")
            return False
        if new_person.l_name == "":
            print("Last name is empty!")
            return False
        return True
            

    def is_exists(self, persons_id):
        people = self.load_data()
        for person in people:
            if int(person.id) == int(persons_id):
                return True
        return False
