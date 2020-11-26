
# import math
# # Task 1
# class Shape:
#     def get_shape_area(self):
#         pass

    
# class Triangle(Shape):
#     def __init__(self, base, height):
#         self.base = base
#         self.height = height

#     def get_shape_area(self):
#         print(f"Площадь треугольника: {(self.base * self.height)//2}")
    

# class Square(Shape):
#     def __init__(self, length):
#         self.length = length

#     def get_shape_area(self):
#         print(f"Площадь квадрата: {self.length * self.length}")


# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def get_shape_area(self):
#         pi = math.pi
#         print(f"Площадь круга: {pi * (self.radius ** 2)}")


# t = Triangle(6, 4)
# t.get_shape_area()

# s = Square(7)
# s.get_shape_area()

# c = Circle(8)
# c.get_shape_area()


# task2
# class Person:
#     def __init__(self, name, surname):
#         self.__name = name
#         self.__surname = surname

#     @property
#     def name(self):
#         return self.__name

#     @property
#     def surname(self):
#         return self.__surname

#     @name.setter
#     def name(self):
#         return self.__name

#     @surname.setter
#     def surname(self):
#         return self.__surname

#     def get_info(self):
#         print(f"Привет, меня зовут {self.__name} {self.__surname}")

# class Employee(Person):
#     def __init__(self, name, surname, company, position):
#         super().__init__(name, surname)
#         self.company = company
#         self.position = position

#     def get_info(self):
#         print(f"Привет, меня зовут {self.name} {self.surname}, я работаю в компании {self.company} на должности {self.position}")

# class Student(Person):
#     def __init__(self, name, surname, university ,course):
#         super().__init__(name, surname)
#         self.university = university
#         self.course = course
#     def get_info(self):
#         print(f"Привет, меня зовут {self.name} {self.surname}, я учусь в {self.university} на {self.course} курсе")

# people = [
#     Person("Иван", "Петров"), 
#     Employee("Иван", "Петров", "Рога и копыта", "директор"), 
#     Student("Иван", "Петров", "КГТУ", 3)
#     ]
    
# for person in people:
#     person.get_info()
#     print()

# task3
# class MyInt(int):

#     def get_objects(self, ob1, ob2):
#         print("Это сложение")
#         print(int(ob1) + int(ob2))


# class MyString(str):

#     def get_objects(self, ob1, ob2):
#         print("Это конкатенация")
#         print(str(ob1) + str(ob2))


# num = MyInt()
# num.get_objects(6, '6')
# string = MyString()
# string.get_objects('aka', 51)