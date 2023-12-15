#section programe

#section 1

# n=450
# e=2.71     # e is float 
# print(e)
# print(n)

# length=20
# width=50
# area=length*width
# print(area)
# print(type(length))  # type of length is intger
# print(type(area))    # type of area is string

# num = 50
# if num>=40 : print("50 is biggest ")
# else: print("any thing")
    
# for i in range(10):
#      print(i*2)
#      print(i**2)
#      print(i+5)
     # if i >5:
     #     print(i/2)
        
# i=1
# while i < 100:
#     print(i**2)
#     i += i**2
 

# section 2 


# def hello_world ():
#     print("Hello in Functions")
# hello_world()

# def user (name):
#     return  {name}
# print(user("lolo"))

# def twice (f,x):
#     return (f+x)/3
# print(twice(5, 4))

#section 5
#revision section 4

# class person():
#     def __init__(self, name, age):
#         self.name=name
#         self.age=age
#     def display(self):
#         print(self.name, self.age)
        
# class student(person):
#     def __init__(self, name, age, dod):
#         self.dod=dod
        
#         super().__init__(name, age)
        
#     def displayinfo(self):
#         print(self.name, self.age, self.dod)
        
# obj = student("wing", 19, 25)
# obj.display()
# obj.displayinfo()


#example to show multiple inheritance

# class lol ():
#     def __init__(self):
#         self.str1 = "toot"
#         print("lol")
        
# class lol2 ():
#     def __init__(self):
#         self.str2= "boot"
        
# class wing (lol, lol2):
#     def __init__(self):
        
#         lol.__init__(self)
#         lol2.__init__(self)
        
#     def KKKKK (self):
#         print(self.str1, self.str2)
        
# ob = wing()
# ob.KKKKK()


# class grandfather ():
#     def __init__(self, name):
#         self.name = name
        
#     def getname (self):
#         return self.name
    
# class father (grandfather):
#     def __init__(self, name, age):
#         self.age = age
#         grandfather. __init__ (self,name)
        
#     def getage (self):
#         return self.age

# class me (father):
#     def __init__(self, name, age, address):
#         self.address=address
#         father. __init__(self, name, age)
        
#     def getaddress(self):
#         return self.address, self.age, self.name
    
# allll= me("wing", 19, "egypt")
# print(allll.getaddress())


#access modifier


# class student ():
#     _name = None
    
#     def __init__(self, name):
#         self.name=name
#     def display1 (self):
#         print("Name:" , self.name )
# class newstudent (student):
#     def __init__(self, name):
#         super. __init__(self, name)
        
#     def display2 (self):
#         print(self._name)
        
#         self.display2()
        
        
        
        


































