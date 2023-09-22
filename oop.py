#class student:

    #data members
    #Name, email, phone, ...

    #member functions
    #def __init__(self):               #init function initializes the object's attributes
       # self.name ="santa"
      #  self.email = "santa@christ.in"
     #   self.phone = 95515358738

    #def printStudent(self):
     #   print("Name": {}\nEmail :{},\nPhone: {}".format(
    #          self.name,self.email,self.phone
   #     ))

 #   def __str__(self):
  #      pass


#santa = student()
#santa.printStudent()
#print(santa.name)







class Student:
    def __init__(self,a,b):
        self.name = a
        self.stu_class = b

    def __str__(self):
        return self.name

abc = Student("ben","BBA")
print(abc.name,abc.stu_class)
print(abc)
print(type(abc))