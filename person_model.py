
class Person:

    def __init__(self, id:int, f_name, l_name):
        self.id = id
        self.f_name = f_name
        self.l_name = l_name

    @staticmethod
    def from_row(row):
        id = row['id'] 
        f_name = row['first_name']
        l_name = row['last_name']
        return Person(id, f_name, l_name)
    
    def to_write_row(self):
        return [{'id': self.id, 'first_name': self.f_name, 'last_name': self.l_name}]

    def __str__(self):
        return "{:<5}{:<15}{:<20}".format(self.id, self.f_name, self.l_name)