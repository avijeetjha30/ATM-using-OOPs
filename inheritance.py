####################### Inheritance ##############################
# class User:
#     def login(self):
#         print("Login")
#     def register(self):
#         print("Register")

# class Student(User):
#     def enrol(self):
#         print("Enrol")
#     def review(self):
#         print("Review")

# class Instructor(User):
#     def create(self):
#         print("Create video")
#     def comment(self):
#         print("Commented")

# stu1 = Student()
# stu1.login()

# in1 = Instructor()
# in1.login()


####################### Inheriting Constructor ##############################

# class User:
#     def __init__(self,name,email):
#         self.name = "kumar"
#         self.email = email

# class Student(User):
#     # def __init__(self,name,email):
#     #     self.name = name
#     #     self.email = email
#     def register(self):
#         print("Registerd")

# s = Student("avi","123")
# print(s.name)

####################### Inheriting Private data ##############################

# class User:
#     def __init__(self,name,email):
#         self.name = name
#         self.__email = email

# class Student(User):
#     def register(self):
#         print("Registerd")

# s = Student("avi","123")
# print(s.name)
# # print(s.__email)
# # print(s._Student__email)
# # print(s._User__email)

####################### Question on privet class ##############################

# class User:
#     def __init__(self,name,email):
#         self.name = name
#         self.__email = email
    
#     def get_email(self):
#         print(self.__email)

# class Student(User):
#     def register(self):
#         print("Registerd")

# s = Student("avi","123")
# print(s.name)
# s.get_email()

####################### Polymorphism Mehod overriding ##############################

# class User:
#     def __init__(self,name,email):
#         self.name = name
#         self.__email = email
    
#     def register(self):
#         print("We are in User register")

# class Student(User):
#     def register(self):
#         print("We are in Student register")

# s = Student("avi","123")
# print(s.name)
# print(s.register())


####################### Super Keyword for overriding ##############################

# class User:
#     def __init__(self,name,email):
#         self.name = name
#         self.__email = email
    
#     def register(self):
#         print("We are in User register")

# class Student(User):
#     def register(self):
#         print("We are in Student register")
#         super().register()

# s = Student("avi","123")
# print(s.name)
# s.register()

####################### Super Keyword with constructor ##############################

# class User:
#     def __init__(self,name,email):
#         self.name = name
#         self.email = email
    
#     def register(self):
#         print("We are in User register")

# class Student(User):
#     def __init__(self,name,email,section,college):
#         super().__init__(name,email)
#         self.section = section
#         self.college = college

#     def register(self):
#         print("We are in Student register")
#         super().register()

# s = Student("avi","123","a","pce")
# print(s.name)
# s.section

####################### super method on privet class ##############################

class User:
    def __init__(self,name):
        self.__name = name
    
    def get_name(self):
        print(self.__name)

class Student(User):
    def __init__(self,name,email):
        super().__init__(name)
        self.__email = email
        # super().__init__(name)
    
    def get_email(self):
        print(self.__email)

s = Student("avi","123")
s.get_name()
s.get_email()