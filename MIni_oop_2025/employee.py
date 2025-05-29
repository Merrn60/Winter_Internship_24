class Employee:
    def __init__(self ,emp_id ,name ,position,salary,):
        self.emp_id=emp_id
        self.name=name
        self.salary=salary
        self.position = position
        self.projects=[]

    def update_info(self,name, position, salary):
        if name is not None:
            self.name=name
        if position is not None:
            self.position=position
        if salary is not None:
            self.salary=salary


    def assign_project(self,project_id):
        if project_id not in self.projects:
            self.projects.append(project_id)


    def  remove_project(self,project_id):
        if project_id in self.projects:
            self.projects.remove(project_id)

    def get_details(self):
        return "{"+f"'ID' : {self.emp_id} " +", "+ f"'NAME' :'{self.name}'"+", "+f"'POSITION' :'{self.position}' " +", "+f"'SALARY' :{ self.salary}"+", "+f"'PROJECTS': {self.projects} "+"}"








