from datetime import date


class Person:
    
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
    
    @classmethod
    def details(cls, name, year):
        return name, date.today().year - year
    
    def check_age(self):
        return self.age > 19


