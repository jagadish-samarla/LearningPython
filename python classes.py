class Person:
    """An example to class to hold a person name and age """

    def __int__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return self.name + ' is ' + str(self.age)

    def birthday(self):
        print('Happy BirthDay!!, You were ', self.age)
        self.age += 1
        print('you are', self.age, 'now')

    def calculate_pay(self, hours_worked):
        rate_of_pay = 7.5
        if self.age >= 21:
            rate_of_pay += 2.5
        return hours_worked * rate_of_pay

    def is_teenager(self):
        return self.age < 20


p1 = Person()
p1.name = "john"
p1.age = 36
#print(p1)
#p1.__str__()
#p1.birthday()
#rint(p1)
#p1.age = 18
#print(p1)

print("class attrbutes")
print(Person.__name__)
print(Person.__module__)
print(Person.__doc__)
print(Person.__dict__)
print("object attributes")
print(p1.__class__)
print(p1.__dict__)