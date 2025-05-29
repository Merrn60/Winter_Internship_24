class Department:
    def __init__(self,dep_id,name):
         self.dep_id = dep_id
         self.name = name
         self.mang_id = None
         self.employees =[]


    def assign_manager(self,mang_id):
        self.mang_id =mang_id



    def add_employee(self,emp_id):
        if emp_id not in self.employees:
            self.employees.append(emp_id)


    def remove_employee(self,emp_id):
        if emp_id in self.employees:
         self.employees.remove(emp_id)

    def  get_department_details(self):
        return "{"+f" 'ID' : {self.dep_id}"+" ,"+f"'Name' : '{self.name}'"+" ,"+f"'ManagerID' :{self.mang_id}"+", "+f"'Employees' :{self.employees}"+"}"