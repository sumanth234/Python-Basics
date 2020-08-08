

class Student :
    def __init__(self,name):
        self.name = name;
        self.marks = [];

    def average(self):
        return sum(self.marks) / len(self.marks)


class WorkingStudent(Student): #WorkingStudent extend/inherits from class Student
    def __init__(self,name,salary):
        super().__init__(name) # Calling init method of parent class to initialise self
        self.salary = salary;

    def getSalary(self):
        return self.salary;

    @property # this decorator is used for function with no arguments ans siumple return output
    def getsalary(self):
        return self.salary;

x = WorkingStudent('X',10000)
x.marks.append(100);
x.marks.append(99)

print(x.average()); #Accessinf Method of parent class

print(x.getSalary()); #Accessing method of child

print(x.getsalary); #Since you are using @property decorator,no need to call it as a function call and you can directly access
